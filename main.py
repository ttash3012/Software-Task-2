import random

# -----------------------------
# PLAYER CLASS
# -----------------------------
class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack = 20
        self.inventory = []
        self.location = None

    def show_stats(self):
        print("\n========== PLAYER ==========")
        print("Name:", self.name)
        print("Health:", self.health)
        print("Attack:", self.attack)
        print("Inventory:", self.inventory)
        print("============================")

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def heal(self):
        if "Health Potion" in self.inventory:
            self.inventory.remove("Health Potion")
            self.health += 30
            if self.health > 100:
                self.health = 100
            print("You used a Health Potion.")
        else:
            print("You don't have a Health Potion.")

    def is_alive(self):
        return self.health > 0


# -----------------------------
# ENEMY CLASS
# -----------------------------
class Enemy:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def take_damage(self, damage):
        self.health -= damage

    def is_alive(self):
        return self.health > 0


# -----------------------------
# ROOM CLASS
# -----------------------------
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.item = None
        self.enemy = None

    def connect(self, direction, room):
        self.connections[direction] = room

    def display(self):
        print("\n===================================")
        print(self.name)
        print("-----------------------------------")
        print(self.description)

        if self.item:
            print("\nItem Found:", self.item)

        if self.enemy and self.enemy.is_alive():
            print("Enemy:", self.enemy.name)

        print("\nExits:")
        for direction in self.connections:
            print("-", direction)

        print("===================================")


# -----------------------------
# GAME CLASS
# -----------------------------
class Game:

    def __init__(self):

        print("===================================")
        print("      THE LOST KINGDOM")
        print("===================================")

        name = input("Enter your hero's name: ")

        self.player = Player(name)

        # Create rooms
        self.village = Room(
            "Village",
            "A peaceful village surrounded by mountains."
        )

        self.forest = Room(
            "Forest",
            "A dark forest filled with dangerous creatures."
        )

        self.cave = Room(
            "Crystal Cave",
            "A cave containing ancient treasures."
        )

        self.castle = Room(
            "Dark Castle",
            "The Dark Wizard lives here."
        )

        # Connect rooms
        self.village.connect("north", self.forest)

        self.forest.connect("south", self.village)
        self.forest.connect("east", self.cave)

        self.cave.connect("west", self.forest)
        self.cave.connect("north", self.castle)

        self.castle.connect("south", self.cave)

        # Items
        self.forest.item = "Iron Sword"
        self.cave.item = "Magic Key"

        # Enemies
        self.forest.enemy = Enemy("Goblin", 40, 10)
        self.castle.enemy = Enemy("Dark Wizard", 100, 20)

        self.player.location = self.village

    # -----------------------
    # GAME LOOP
    # -----------------------

    def start(self):

        print("\nWelcome,", self.player.name)

        while self.player.is_alive():

            room = self.player.location

            room.display()

            print("\nCommands")
            print("move")
            print("take")
            print("heal")
            print("stats")
            print("quit")

            command = input("\n> ").lower()

            if command == "stats":
                self.player.show_stats()

            elif command == "heal":
                self.player.heal()

            elif command == "take":

                if room.item:
                    print("You picked up", room.item)
                    self.player.inventory.append(room.item)

                    if room.item == "Iron Sword":
                        self.player.attack = 35

                    room.item = None

                else:
                    print("Nothing to take.")

            elif command == "move":

                direction = input("Direction: ").lower()

                if direction in room.connections:

                    self.player.location = room.connections[direction]

                    if self.player.location.enemy:
                        self.battle(self.player.location.enemy)

                else:
                    print("You can't go that way.")

            elif command == "quit":
                print("Goodbye!")
                break

            else:
                print("Invalid command.")

        print("\nGame Over")


# -----------------------------
# START GAME
# -----------------------------

game = Game()
game.start()

    # -----------------------
    # BATTLE SYSTEM
    # -----------------------

    def battle(self, enemy):

        print(f"\n⚔ A {enemy.name} appears!")

        while enemy.is_alive() and self.player.is_alive():

            print("\n======================")
            print(f"{self.player.name}: {self.player.health} HP")
            print(f"{enemy.name}: {enemy.health} HP")
            print("======================")

            print("\nChoose an action:")
            print("1 - Attack")
            print("2 - Heal")
            print("3 - Run")

            choice = input("> ")

            if choice == "1":

                damage = random.randint(
                    self.player.attack - 5,
                    self.player.attack + 5
                )

                enemy.take_damage(damage)

                print(f"\nYou hit the {enemy.name} for {damage} damage!")

                if enemy.is_alive():

                    enemy_damage = random.randint(
                        enemy.attack - 3,
                        enemy.attack + 3
                    )

                    self.player.take_damage(enemy_damage)

                    print(f"The {enemy.name} hits you for {enemy_damage} damage!")

            elif choice == "2":

                self.player.heal()

                if enemy.is_alive():

                    enemy_damage = random.randint(
                        enemy.attack - 3,
                        enemy.attack + 3
                    )

                    self.player.take_damage(enemy_damage)

                    print(f"The {enemy.name} attacks while you heal!")

            elif choice == "3":

                if enemy.name == "Dark Wizard":
                    print("You cannot escape the final battle!")

                else:
                    print("You escaped safely.")
                    return

            else:
                print("Invalid choice.")

        # Enemy defeated

        if self.player.is_alive():

            print(f"\n✓ You defeated the {enemy.name}!")

            if enemy.name == "Goblin":

                print("The Goblin dropped a Health Potion!")

                self.player.inventory.append("Health Potion")

            elif enemy.name == "Dark Wizard":

                print("\n===============================")
                print("🏆 CONGRATULATIONS!")
                print("===============================")
                print("You defeated the Dark Wizard!")
                print("Peace has returned to")
                print("The Lost Kingdom!")
                print("===============================")

                quit()

        else:

            print("\n===============================")
            print("☠ GAME OVER")
            print("===============================")
            print("The Dark Wizard has won...")
            print("===============================")

            quit()
