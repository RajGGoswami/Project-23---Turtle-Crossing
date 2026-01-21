from turtle import Turtle
import random

# Predefined colors for car variety
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

# Initial car movement speed
STARTING_MOVE_DISTANCE = 5

# Speed increase per level
MOVE_INCREMENT = 10


class CarManager(Turtle):
    """
    The CarManager class is responsible for:
    - Creating cars at random intervals
    - Moving all cars across the screen
    - Increasing car speed as levels progress
    """

    def __init__(self):
        self.all_cars = []
        self.starting_move_distance = 5

    def create_car(self):
        """
        Randomly creates a new car.
        A 1-in-6 chance ensures cars spawn unpredictably.
        """
        chance = random.randint(1, 6)
        if chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randint(-250, 250))
            self.all_cars.append(new_car)

    def move_car(self):
        """Moves all cars from right to left across the screen."""
        for car in self.all_cars:
            car.backward(self.starting_move_distance)

    def increase_speed(self):
        """Increases car movement speed when the player levels up."""
        self.starting_move_distance += 10
