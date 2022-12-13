from game.casting.actor import Actor


class HealthDisplay(Actor):
    """
    A record of the spaceship's health.
    
    The responsibility of HealthDisplay is to display the health of the player's spaceship.
    It contains methods for adding and getting health. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self):
        super().__init__()
        self._text = "Health"

     


    