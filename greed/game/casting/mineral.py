import random

from game.casting.actor import Actor
from game.shared.color import Color
from game.shared.point import Point

class Mineral(Actor):
    """An mineral is either a gem or rock that falls from the top of the
    screen. It inherits from Actor.
    
    Args:
        Actor (Actor): the parent class of Mineral"""

    def __init__(self):
        super().__init__()
        """Constructs a new instance of Mineral from the Actor class.
            
            Args:
                self (Mineral): an instance of Mineral
            """
        self._mineral_type = ""
        self._value = 1

    def get_value(self):
        """Returns point value of the mineral.
        Args:
            self (Mineral): an instance of Mineral
        """
        return self._value

    def rand_properties(self):
        """Sets the mineral's type as either a gem or rock.
        
        Args:
            self (Mineral): an instance of Mineral
        """

        # Change mineral type.
        type = random.randint(1, 10)

        if type == 1:
            self._mineral_type = "gem"
            self._text = "*"
            self._value = 1

        elif type != 1:
            self._mineral_type = "rock"
            self._text = "O"
            self._value = -1

        # Change color.
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        self._color = Color(r, g, b)

        x = random.randint(1, 59) * 15
        y = 0
        new_position = Point(x, y)
        self._position = new_position