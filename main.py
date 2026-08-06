# ==========================================
# Escape the Haunted School
# Software Engineering Assessment
# Part 1 - Classes and Game Setup
# ==========================================

import random

# ----------------------------
# PLAYER CLASS
# ----------------------------

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []

    def show_stats(self):
        print("\n========== PLAYER ==========")
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print("Inventory:", self.inventory)
        print("============================")

    def take_damage(self, amount):
        self.health -= amount

        if self.health < 0:
            self.health = 0

        print(f"\nYou lost {amount} health.")

    def heal(self):

        if "First Aid Kit" in self.inventory:

            self.inventory.remove("First Aid Kit")

            self.health += 30

            if self.health > 100:
                self.health = 100

            print("\nYou used a First Aid Kit.")

        else:
            print("\nYou don't have a First Aid Kit.")

    def is_alive(self):
        return self.health > 0


# ----------------------------
# GHOST CLASS
# ----------------------------

class Ghost:

    def __init__(self, name, damage):
        self.name = name
        self.damage = damage


# ----------------------------
# ROOM CLASS
# ----------------------------

class Room:

    def __init__(self, name, description):

        self.name = name
        self.description = description

        self.item = None
        self.ghost = None

        self.connections = {}

    def connect(self, direction, room):
        self.connections[direction] = room

    def display(self):

        print("\n=================================")
        print(self.name)
        print("=================================")

        print(self.description)

        if self.item:
            print("\nItem Found:", self.item)

        if self.ghost:
            print("Ghost:", self.ghost.name)

        print("\nExits:")

        for direction in self.connections:
            print("-", direction)


# ----------------------------
# GAME CLASS
# ----------------------------

class Game:

    def __init__(self):

        print("===================================")
        print(" ESCAPE THE HAUNTED SCHOOL ")
        print("===================================")

        player_name = input("Enter your name: ")

        self.player = Player(player_name)

        # ------------------------
        # Create Rooms
        # ------------------------

        self.classroom = Room(
            "Classroom",
            "You wake up alone inside an empty classroom."
        )

        self.hallway = Room(
            "Hallway",
            "The hallway is dark and strangely quiet."
        )

        self.library = Room(
            "Library",
            "Rows of dusty books cover the shelves."
        )

        self.science_lab = Room(
            "Science Lab",
            "Broken beakers are scattered everywhere."
        )

        self.principal_office = Room(
            "Principal's Office",
            "This room might contain the Master Key..."
        )

        self.exit = Room(
            "School Exit",
            "The front doors are locked."
        )

        # ------------------------
        # Connect Rooms
        # ------------------------

        self.classroom.connect("east", self.hallway)

        self.hallway.connect("west", self.classroom)
        self.hallway.connect("north", self.library)
        self.hallway.connect("south", self.science_lab)
        self.hallway.connect("east", self.principal_office)

        self.library.connect("south", self.hallway)

        self.science_lab.connect("north", self.hallway)

        self.principal_office.connect("west", self.hallway)
        self.principal_office.connect("east", self.exit)

        self.exit.connect("west", self.principal_office)

        # ------------------------
        # Place Items
        # ------------------------

        self.library.item = "Flashlight"

        self.science_lab.item = "First Aid Kit"

        self.principal_office.item = "Master Key"

        # ------------------------
        # Place Ghosts
        # ------------------------

        self.library.ghost = Ghost(
            "Library Ghost",
            15
        )

        self.science_lab.ghost = Ghost(
            "Science Ghost",
            20
        )

        # Starting Room

        self.player_location = self.classroom

        # ----------------------------
    # SHOW HELP
    # ----------------------------

    def show_help(self):

        print("\n========== COMMANDS ==========")
        print("move       - Move to another room")
        print("search     - Search the room")
        print("inventory  - View inventory")
        print("heal       - Use a First Aid Kit")
        print("stats      - View player stats")
        print("help       - Show commands")
        print("quit       - Quit game")
        print("==============================")

    # ----------------------------
    # GHOST ENCOUNTER
    # ----------------------------

    def ghost_attack(self):

        room = self.player_location

        if room.ghost:

            print(f"\n👻 {room.ghost.name} appears!")

            damage = random.randint(
                room.ghost.damage - 5,
                room.ghost.damage + 5
            )

            self.player.take_damage(damage)

            if self.player.is_alive():

                print("The ghost disappears into the darkness...")

                room.ghost = None

            else:

                print("\nThe ghost has defeated you...")
                print("GAME OVER")
                quit()

    # ----------------------------
    # SEARCH ROOM
    # ----------------------------

    def search_room(self):

        room = self.player_location

        if room.item:

            print(f"\nYou found a {room.item}!")

            self.player.inventory.append(room.item)

            room.item = None

        else:

            print("\nThere is nothing useful here.")

    # ----------------------------
    # MOVE PLAYER
    # ----------------------------

    def move_player(self):

        room = self.player_location

        direction = input("\nDirection: ").lower()

        if direction in room.connections:

            self.player_location = room.connections[direction]

            self.ghost_attack()

        else:

            print("\nYou can't go that way.")

    # ----------------------------
    # GAME LOOP
    # ----------------------------

    def play(self):

        print("\nWelcome to Escape the Haunted School!")
        print("Type 'help' to see the commands.")

        while self.player.is_alive():

            room = self.player_location

            room.display()

            command = input("\n> ").lower()

            if command == "help":

                self.show_help()

            elif command == "move":

                self.move_player()

            if self.check_win():
        break
            
            elif command == "search":

                self.search_room()

            elif command == "inventory":

                print("\nInventory:")

                if len(self.player.inventory) == 0:

                    print("Empty")

                else:

                    for item in self.player.inventory:

                        print("-", item)

            elif command == "heal":

                self.player.heal()

            elif command == "stats":

                self.player.show_stats()

            elif command == "quit":

                print("\nThanks for playing!")
                break

            else:

                print("\nInvalid command.")

        # ----------------------------
    # CHECK IF PLAYER HAS WON
    # ----------------------------

    def check_win(self):

        # Player reaches the exit
        if self.player_location == self.exit:

            # Check if they have the Master Key
            if "Master Key" in self.player.inventory:

                print("\n======================================")
                print("🎉 CONGRATULATIONS!")
                print("======================================")
                print("You unlocked the front doors.")
                print("You escaped the Haunted School!")
                print("You survived the night!")
                print("======================================")

                return True

            else:

                print("\n🚪 The doors are locked!")
                print("You need to find the Master Key.")

                # Move player back into the Principal's Office
                self.player_location = self.principal_office

        return False

# ==========================================
# START THE GAME
# ==========================================

print("\n======================================")
print("      ESCAPE THE HAUNTED SCHOOL")
print("======================================")
print("You wake up alone inside your school.")
print("Something doesn't feel right...")
print("Find the Master Key and escape!")
print("Be careful... ghosts are watching.")
print("======================================")

game = Game()
game.play()

print("\n======================================")
print("Thank you for playing!")
print("======================================")
