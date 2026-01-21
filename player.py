from turtle import Turtle

# Starting position of the player
STARTING_POSITION = (0, -280)

# Distance moved per key press
MOVE_DISTANCE = 10

# Y-coordinate representing the finish line
FINISH_LINE_Y = 200


class Player(Turtle):
    """
    The Player class represents the user-controlled turtle.
    It handles movement and position resets after each level.
    """

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.seth(90)
        self.goto(STARTING_POSITION)

    def move(self):
        """Moves the player forward."""
        self.forward(MOVE_DISTANCE)

    def reset_position(self):
        """Resets the player back to the starting position."""
        self.goto(STARTING_POSITION)
