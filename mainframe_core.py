import random
import time

# ==========================================
# 1. THE ENVIRONMENT LAYER (NetworkNode Class)
# ==========================================
class NetworkNode:
    """Represents a virtual room/sector inside the corporate mainframe."""
    def __init__(self, node_id, name, description):
        self.node_id = node_id
        self.name = name
        self.description = description
        self.connected_nodes = []  # Array holding links to adjacent Node objects

    def link_node(self, other_node):
        """Creates a two-way connection between network nodes."""
        if other_node not in self.connected_nodes:
            self.connected_nodes.append(other_node)
        if self not in other_node.connected_nodes:
            other_node.connected_nodes.append(self)


# ==========================================
# 2. THE ENTITY LAYER (OOP Parent Class)
# ==========================================
class SystemEntity:
    """Master template for active digital entities inside the system."""
    def __init__(self, name, starting_node):
        self.name = name
        self.current_node = starting_node  # Holds a reference to a NetworkNode object

    def change_location(self, target_node):
        """Updates the entity's position array."""
        self.current_node = target_node


# ==========================================
# 3. INHERITANCE IN ACTION (OOP Child Classes)
# ==========================================
class Player(SystemEntity):
    """Child class handling player states, RAM, and exploit inventory."""
    def __init__(self, name, starting_node):
        # Call the parent class constructor
        super().__init__(name, starting_node)
        self.ram_slots = 100
        self.exploits = 3  # Your "arrows" to delete the Wumpus AI

    def scan_network(self):
        """Scans adjacent nodes for traces of threats or hazards (Wumpus Clues)."""
        print("\n[SYSTEM] Running diagnostic ping on adjacent nodes...")
        time.sleep(0.4)
        
        has_ai = False
        has_ice = False
        
        for neighbor in self.current_node.connected_nodes:
            # Check if Hostile AI is in a neighboring node object
            if hasattr(neighbor, 'has_ai') and neighbor.has_ai:
                has_ai = True
            # Check if an ICE trap is nearby
            if hasattr(neighbor, 'has_ice') and neighbor.has_ice:
                has_ice = True

        if has_ai:
            print("⚠️ WARNING: Severe ping latency detected nearby. Hostile AI signature present.")
        if has_ice:
            print("⚡ ALERT: Data packet leakage detected. High danger of ICE security traps.")
        if not has_ai and not has_ice:
            print("🟢 Status: Signal clear. No immediate threats detected in adjacent nodes.")


class HostileAI(SystemEntity):
    """Child class representing the tracking AI (The Wumpus)."""
    def __init__(self, name, starting_node):
        super().__init__(name, starting_node)
        starting_node.has_ai = True  # Flag the node object


# ==========================================
# 4. GAME ENGINE LOGIC (Main Game Class)
# ==========================================
class MainframeEngine:
    """Manages map generation, input loops, and win/loss states."""
    def __init__(self):
        self.nodes = []
        self.player = None
        self.ai = None
        self.setup_mainframe()

    def setup_mainframe(self):
        """Generates nodes, populates traps, and instantiates objects."""
        # Create 6 distinct node objects
        names = ["Core Mainframe", "Data Vault", "Sub-Routing Node", "Encryption Gate", "Proxy Server", "Backdoor Terminal"]
        descs = [
            "The heart of the network. High-density data streams flow everywhere.",
            "Cold storage. Thousands of locked encrypted archives sit silently.",
            "A messy web of optical fiber switchboards flashing red and green.",
            "A secure checkpoint flashing firewall security requests.",
            "A decoy node routing anonymous external traffic through the web.",
            "An old, forgotten maintenance port covered in legacy code lines."
        ]
        
        for i in range(6):
            self.nodes.append(NetworkNode(i + 1, names[i], descs[i]))

        # Establish network grid sequences (Linking nodes together)
        self.nodes[0].link_node(self.nodes[1])
        self.nodes[0].link_node(self.nodes[2])
        self.nodes[1].link_node(self.nodes[3])
        self.nodes[2].link_node(self.nodes[4])
        self.nodes[3].link_node(self.nodes[5])
        self.nodes[4].link_node(self.nodes[5])

        # Setup Traps (ICE Traps) on random empty nodes
        self.nodes[2].has_ice = True
        self.nodes[4].has_ice = True

        # Instantiate entities (Player starts at Node 6, AI hides at Node 1)
        self.player = Player("Rogue_Hacker", self.nodes[5])
        self.ai = HostileAI("V_I_R_U_S", self.nodes[0])

    def start_game(self):
        print("=" * 60)
        print("        MAINFRAME INFILTRATOR: OOP PYTHON EDITION")
        print("=" * 60)
        print("Objective: Locate and delete the Hostile AI before it traces you.")
        print("Watch out for ICE security traps that damage your RAM grid.")
        
        while self.player.ram_slots > 0:
            print(f"\n--- CURRENT LOCATION: {self.player.current_node.name} (Node {self.player.current_node.node_id}) ---")
            print(self.player.current_node.description)
            
            # Run OOP Scanner Method
            self.player.scan_network()
            
            # Print connection choices
            valid_ids = [n.node_id for n in self.player.current_node.connected_nodes]
            print(f"Available Connections to Hop: {valid_ids}")
            print(f"RAM Integrity: {self.player.ram_slots}% | Exploit Scripts Left: {self.player.exploits}")
            
            action = input("\nChoose Action - [M]ove to a node or [D]eploy exploit script: ").strip().upper()
            
            if action == 'M':
                try:
                    target_id = int(input("Enter Node ID to jump into: "))
                    if target_id in valid_ids:
                        # Find the actual node object from the ID
                        next_node = next(n for n in self.nodes if n.node_id == target_id)
                        self.player.change_location(next_node)
                        
                        # Process movement logic & traps
                        if hasattr(next_node, 'has_ai') and next_node.has_ai:
                            print("\n❌ CRITICAL FAILURE! You jumped directly into the Hostile AI's layer.")
                            print("Your terminal was bricked instantly. Trace-wiped. GAME OVER.")
                            return
                        
                        if hasattr(next_node, 'has_ice') and next_node.has_ice:
                            print("\n⚡ ZAP! You stepped into an active ICE Security Trap!")
                            self.player.ram_slots -= 40
                            print("System Warning: Countermeasures hit your RAM slots. -40% integrity.")
                            
                    else:
                        print("Invalid path! Those system nodes are not linked.")
                except ValueError:
                    print("Error: Input must be a numerical Node ID.")
                    
            elif action == 'D':
                if self.player.exploits > 0:
                    try:
                        target_id = int(input("Enter target Node ID to drop the logic bomb into: "))
                        self.player.exploits -= 1
                        
                        # Find targeted node object
                        target_node = next(n for n in self.nodes if n.node_id == target_id)
                        
                        if hasattr(target_node, 'has_ai') and target_node.has_ai:
                            print("\n✨ SUCCESS! Your Decompressor exploit executed flawlessly.")
                            print(f"The Hostile AI '{self.ai.name}' was purged from the mainframe.")
                            print("YOU WIN: System cleared. Logged off safely.")
                            return
                        else:
                            print("\n💨 Missed! The target node was empty. Your script dissolved into dead space.")
                            # Wumpus logic: AI moves to a random adjacent node if you miss
                            current_ai_node = self.ai.current_node
                            current_ai_node.has_ai = False
                            new_ai_node = random.choice(current_ai_node.connected_nodes)
                            self.ai.change_location(new_ai_node)
                            new_ai_node.has_ai = True
                            print("🚨 ALERT: The sound of the exploit execution caused the AI to shift locations!")
                    except ValueError:
                        print("Input must be a numerical Node ID.")
                else:
                    print("No exploit scripts remaining in memory cache!")
            else:
                print("Unknown command console directive.")
                
        print("\n❌ SYSTEM BREAKDOWN: Your RAM integrity hit 0%. Your terminal overloaded. GAME OVER.")

# Execute game runtime
if __name__ == "__main__":
    game = MainframeEngine()
    game.start_game()
