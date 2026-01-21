# Project-23---Turtle-Crossing

This project is inspired by the classic Frogger-style crossing game, built as part of my 100 Days of Code (Python) journey.

**Project Overview**

The goal of the game is simple:

Move the turtle from the bottom of the screen to the top

Avoid randomly spawning cars

Each successful crossing increases difficulty

**Why this project exists**

This project was built to practice:

Game loops and real-time animation

Object interaction and collision detection

Difficulty scaling using speed increments

Clean separation of responsibilities using classes

Keyboard input handling with Turtle

**What I learned**

How to manage many moving objects efficiently

Why randomness improves gameplay realism

How to scale difficulty without changing game rules

How multiple classes coordinate inside a single loop

How to detect collisions using distance checks

**How the game works (high level)**

Screen initializes and disables auto-refresh

Player turtle is created at the bottom

Cars spawn randomly and move across the screen

Collision with a car ends the game

Reaching the top advances the level

Car speed increases after each level

**Project File Structure**

├── main.py         # Main game loop and collision handling

├── player.py       # Player movement and position control

├── car_manager.py  # Car creation, movement, and speed scaling

├── scoreboard.py   # Level tracking and game-over display

**Design Notes**

Cars spawn probabilistically to avoid predictability

Difficulty increases through speed, not volume

Simple mechanics keep gameplay focused and readable

Clean class responsibilities improve maintainability
