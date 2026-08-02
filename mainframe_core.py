class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack = 20
        self.inventory = []
        self.location = None

    def show_stats(self):
        print("\n====== PLAYER ======")
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Attack: {self.attack}")
        print("Inventory:", self.inventory)
        print("====================")

    def add_item(self, item):
        self.inventory.append(item)
        print(f"You picked up {item}!")

    def heal(self, amount):
        self.health += amount
        if self.health > 100:
            self.health = 100
        print(f"You healed {amount} health.")

    def take_damage(self, damage):
        self.health -= damage
        print(f"You lost {damage} health.")

    def is_alive(self):
        return self.health > 0

class Enemy:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def take_damage(self, damage):
        self.health -= damage

    def is_alive(self):
        return self.health > 0


class Goblin(Enemy):
    def __init__(self):
        super().__init__("Goblin", 40, 10)


class DarkWizard(Enemy):
    def __init__(self):
        super().__init__("Dark Wizard", 100, 20)

class Item:
    def __init__(self, name):
        self.name = name


class Potion(Item):
    def __init__(self):
        super().__init__("Health Potion")


class Sword(Item):
    def __init__(self):
        super().__init__("Iron Sword")


class Key(Item):
    def __init__(self):
        super().__init__("Magic Key")

class Room:

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connected_rooms = {}
        self.item = None
        self.enemy = None

    def connect(self, direction, room):
        self.connected_rooms[direction] = room

    def show_room(self):
        print("\n==========")
        print(self.name)
        print(self.description)
        print("==========")

        if self.item:
            print("Item:", self.item.name)

        if self.enemy:
            print("Enemy:", self.enemy.name)

        print("\nExits:")
        for direction in self.connected_rooms:
            print("-", direction)

from player import Player
from room import Room
from item import Sword, Potion, Key
from enemy import Goblin, DarkWizard


class Game:

    def __init__(self):

        name = input("Enter your name: ")
        self.player = Player(name)

        village = Room("Village", "A peaceful village.")
        forest = Room("Forest", "A dark forest.")
        cave = Room("Cave", "A cold cave.")
        castle = Room("Dark Castle", "The Dark Wizard waits.")

        village.connect("north", forest)
        forest.connect("south", village)
        forest.connect("east", cave)
        cave.connect("west", forest)
        cave.connect("north", castle)
        castle.connect("south", cave)

        forest.item = Sword()
        cave.item = Key()

        forest.enemy = Goblin()
        castle.enemy = DarkWizard()

        self.player.location = village

    def play(self):

        print("\nWelcome to The Lost Kingdom!")

        while self.player.is_alive():

            room = self.player.location
            room.show_room()

            command = input("\nCommand (move/take/stats/quit): ").lower()

            if command == "stats":
                self.player.show_stats()

            elif command == "take":

                if room.item:
                    self.player.add_item(room.item.name)
                    room.item = None
                else:
                    print("Nothing to take.")

            elif command == "move":

                direction = input("Direction: ").lower()

                if direction in room.connected_rooms:
                    self.player.location = room.connected_rooms[direction]

                    if self.player.location.enemy:
                        self.fight(self.player.location.enemy)

                else:
                    print("You can't go that way.")

            elif command == "quit":
                break

    def fight(self, enemy):

        print(f"\nA {enemy.name} attacks!")

        while enemy.is_alive() and self.player.is_alive():

            enemy.take_damage(self.player.attack)
            print(f"You hit the {enemy.name}")

            if enemy.is_alive():
                self.player.take_damage(enemy.attack)

        if self.player.is_alive():
            print(f"You defeated the {enemy.name}!")

            if enemy.name == "Dark Wizard":
                print("\nCongratulations!")
                print("You saved the Lost Kingdom!")
                quit()

from game import Game

game = Game()
game.play()
