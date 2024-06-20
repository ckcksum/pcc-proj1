# Alien Invasion
This is my solution to the Python Crash Course Part II Project 1, Alien Invasion.

---
- [TOC](#toc)
- [Alien Invasion](#alien-invasion)
  - [Planning](#planning)
  - [Description](#description)
    - [Chapter 12 A SHIP THAT FIRES BULLETS](#chapter-12-a-ship-that-fires-bullets)
    - [Chapter 13 ALIENS!](#chapter-13-aliens)
    - [Chapter 14 Scoring](#chapter-14-scoring)

---

## Planning
- **Player**: controls the rocket ship at the bottom center 
  - arrow key: ship to right/left
  - spacebar: shoot bullets
- **A fleet of aliens**: 
  - Fills the sky and moves across and down the screen at the start of the game.
  - All aliens are destroyed: a new and faster fleet appears
- **Losing a ship** :
    - If an alien hits the ship
    - If an alien reaches the bottom of the screen
- **Game end**: Player loses 3 ships

## Description
### Chapter 12 A SHIP THAT FIRES BULLETS
- Create the basic structure of the game include:
  - Game backgroud
  - Ship and bullets settings and control

### Chapter 13 ALIENS!
- Create aliens and the move of the fleet
- Track game statistics with `game_active` flag

### Chapter 14 Scoring
- Set Game Play button
- Elements' speed settings
- Implementing the scoring system

---
[TOP](#toc)
