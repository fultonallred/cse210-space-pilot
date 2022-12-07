from game.casting.actor import Actor

class Scoreboard(Actor):
    """Keeps track of score."""

    def __init__(self):
        super().__init__()
        """Construct a new instance of Scoreboard.
        
        Args:
            self (Scoreboard): an instance of scoreboard.
        """
        self._points = 0

    def add_points(self, points):
        """Adds points.
        
        Args:
            self (Scoreboard): an instance of scoreboard
            points (int) the amount of points to add
        """
        self._points += points

    def subtract_points(self, points):
        """Subtracts points.
        
        Args:
            self (Scoreboard): an instance of Scoreboard
            points (int): points to be subtracted
        """
        self._points -= points

    def get_points(self):
        return self._points