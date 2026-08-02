# Requirements Definition

## Aim

The aim of this project is to develop a text-based role-playing adventure game called **The Lost Kingdom** using **Python** and **Object-Oriented Programming (OOP)**. The game will provide an interactive experience where players explore a fantasy world, battle enemies, collect items, and complete quests to defeat the Dark Wizard and restore peace to the kingdom.

---

# Functional Requirements

## Player System
- The player must be able to enter their name and start a new game.
- The player must have health, an inventory, and a current location.
- The player must be able to move between different locations.

## Navigation
- The game must allow the player to travel between connected rooms.
- Invalid movement choices must display an error message.

## Combat System
- The player must be able to fight enemies.
- Enemies must be able to attack the player.
- The game must calculate damage and update player and enemy health.

## Inventory System
- The player must be able to collect items.
- Items can be stored in the player's inventory.
- The player can use items such as health potions during gameplay.

## Characters
- The game must include multiple characters, including enemies and non-player characters (NPCs).
- Each character must have attributes such as health and damage.

## Game Progress
- The player must complete objectives to reach the final boss.
- The game must display a victory message when the Dark Wizard is defeated.
- The game must end if the player's health reaches zero.

---

# Non-Functional Requirements

## Performance
- The game should respond to player commands without noticeable delay.

## Usability
- Commands and instructions should be simple and easy to understand.
- Error messages should clearly explain invalid inputs.

## Reliability
- The game should run without crashing during normal gameplay.

## Readability
- The code should be organised using classes, methods, and comments so it is easy to read and maintain.

---

# Constraints

## Technology
- The project must be developed using Python.
- The program must use Object-Oriented Programming principles.
- Development will be completed using Visual Studio Code and GitHub.

## Resources
- Only free software and tools may be used.
- The project must be submitted through GitHub.

## Time
- The project must be completed by the assessment due date.

---

# Data Requirements

The game will use several data structures to store information, including:

- Lists for player inventory.
- Dictionaries for room connections and game data.
- Objects to represent the player, enemies, rooms, and items.

---

# Acceptance Criteria

The project will be successful if:

- The player can successfully move between rooms.
- Combat works correctly and updates health values.
- Items can be collected and used.
- The inventory stores collected items correctly.
- The game includes multiple classes and objects.
- The game demonstrates Object-Oriented Programming concepts such as classes, objects, attributes, and methods.
- The player can win by defeating the Dark Wizard or lose if their health reaches zero.
- The project is uploaded to GitHub with regular commits throughout development.
