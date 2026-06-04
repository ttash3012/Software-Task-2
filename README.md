# Software-Task-2

# Task 2: OOP Text-Based RPG — Mainframe Infiltrator

## Project Overview
This repository contains a functional, text-based Cyberpunk RPG written in Python using **Object-Oriented Programming (OOP)**. Inspired by Gregory Yob’s classic *Hunt the Wumpus*, this project remakes the vintage procedural architecture into a clean, modern OOP framework. 

In this game, the player acts as a rogue hacker infiltrating a secure corporate mainframe to delete a hostile, tracking AI (The Wumpus) before their local terminal gets trace-wiped.

### Core Objectives Met
* **OOP Paradigm Implementation:** Designed using inheritance, encapsulation, and clear modular structure.
* **Industry-Standard Documentation:** Includes structured system files, data dictionaries, and engineering journals.
* **Testing Suite Verification:** Validated code execution paths via Black Box, White Box, and Grey Box methods.
* **Version Control Integration:** Developed using explicit Git commit workflows.

---

## Cyberpunk Game Architecture (OOP Suitability)

Procedural languages require messy, massive blocks of nested `if/else` statements to keep track of network rooms, players, and security AI positions. Moving to an **Object-Oriented** structure allows us to bundle variables and functions into clean, independent digital packages.

### 1. Classes and Objects Breakdown
* **The Environment Layer (`NetworkNode` Class):** Every virtual room in the mainframe is an object generated from this class. It contains attributes like `node_id`, `node_name`, a description, and an array linking it to neighboring nodes.
* **The Entity Layer (`SystemEntity` Parent Class):** A master template holding baseline data common to all active entities inside the system (e.g., current location node, entity name).
* **Inheritance in Action (`Player` & `HostileAI` Child Classes):** * The `Player` class inherits location logic from `SystemEntity` but adds its own unique attributes like an `inventory` array (to hold decryption exploits and security bypass keys).
  * The `HostileAI` class inherits basic positions but adds specific behavioral scripts to ambush or track the player.

### 2. Interactions and Methods
Objects interact inside the environment through explicit class behaviors:
* `move_node(target_node)`: Updates coordinates when navigating firewalls.
* `scan_adjacent()`: Pulls data from neighboring node objects to check for latency spikes or packet leaks (the "Wumpus clues").
* `deploy_exploit()`: Triggered when a player drops a logic-bomb script into a target node to terminate the hostile AI.

---

## Data Structures & Logic Examples

### Python Object Class Setup
```python
class SystemEntity:
    """Parent template for all active digital entities in the mainframe."""
    def __init__(self, name, node_location):
        self.name = name
        self.node_location = node_location  # Stores the current Node object

class Player(SystemEntity):
    """Child class inheriting from SystemEntity with inventory capabilities."""
    def __init__(self, name, node_location):
        super().__init__(name, node_location)
        self.ram_slots = 100
        self.exploit_inventory = ["Decompressor.sh"]

    def running_processes(self):
        return f"Active Exploit: {self.exploit_inventory[0]}"
