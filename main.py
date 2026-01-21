# Day 23 – Turtle Crossing
# This project recreates a Frogger-style crossing game using Turtle graphics.
# The player must cross the road while avoiding moving cars.

from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random
import time

# -------------------- Screen Setup --------------------
# The screen acts as the game window and main loop controller
screen = Screen()
screen.setup(width=600, height=600)

# Disable automatic screen updates for smoother animations
screen.tracer(0)

# -------------------- Game Objects --------------------
# Player represents the turtle trying to cross the road
player = Player()

# CarManager handles creation, movement, and speed of cars
car_manager = CarManager()

# Scoreboard tracks the current level and game-over state
score_board = Scoreboard()

# -------------------- Player Controls --------------------
# Player moves forward using the Up arrow key
screen.listen()
screen.onkey(player.move, "Up")

game_on = True

# -------------------- Main Game Loop --------------------
# Runs continuously while the game is active
while game_on:
    # Controls the overall game speed
    time.sleep(0.1)
    screen.update()

    # Randomly creates new cars at the right edge of the screen
    car_manager.create_car()

    # Moves all existing cars across the screen
    car_manager.move_car()

    # -------------------- Collision Detection --------------------
    # Check if the player collides with any car
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            score_board.game_over()
            game_on = False

    # -------------------- Level Progression --------------------
    # If player reaches the finish line:
    # - reset player position
    # - increase level
    # - increase car speed
    if player.ycor() > 280:
        player.reset_position()
        score_board.score += 1
        score_board.update_score()
        car_manager.increase_speed()

# Keeps the window open until user interaction
screen.exitonclick()
