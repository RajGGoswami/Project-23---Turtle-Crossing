from turtle import Turtle

# Font configuration for score display
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """
    The Scoreboard class displays the current level
    and handles the game-over message.
    """

    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.score = 1
        self.goto(-200, 250)
        self.color("black")
        self.write(f"Level: {self.score}", align="center", font=FONT)

    def update_score(self):
        """Updates the displayed level."""
        self.clear()
        self.write(f"Level: {self.score}", align="center", font=FONT)

    def game_over(self):
        """Displays the GAME OVER message at the center of the screen."""
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
