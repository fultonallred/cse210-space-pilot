import random
import constants
from game.shared.color import Color
from game.shared.point import Point
from game.casting.actor import Actor

class Mineral(Actor):
    """An mineral is either a gem or rock that falls from the top of the
    screen. It inherits from Actor.
    
    Args:
        Actor (Actor): the parent class of Mineral
        
    Attributes:
        type (str) the kind of mineral
        value (int) what is added to score if collided with"""

    def __init__(self):
        super().__init__()
        """Constructs a new instance of Mineral from the Actor class.
            
            Args:
                self (Mineral): an instance of Mineral

            Attributes:
                mineral_type (str): what type of mineral it is
                value (int): the points it is worth
                at_bottom (bool): whether it is at the bottom of the screen
            """
        self._mineral_type = ""
        self._value = 1
        self._at_bottom = False
        self._prepare_mineral()


    def _prepare_mineral(self):
        """Sets attributes of the mineral."""

        speed = random.randint(1, 5)
        mineral_velocity = Point(0, speed)
        
        x = random.randint(1, constants.COLUMNS - 1)
        y = 0
        position = Point(x, y)
        position = position.scale(constants.CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
      
        self.set_font_size(constants.FONT_SIZE)
        self.set_color(color)
        self.set_position(position)
        self.set_velocity(mineral_velocity)
        self.set_text("#")

    def move_next(self):
        """Moves the mineral to its next position."""

        x = (self._position.get_x() + self._velocity.get_x()) % constants.MAX_X
        y = (self._position.get_y() + self._velocity.get_y()) % constants.MAX_Y
        self._position = Point(x, y)
        
        if constants.MAX_Y - self._position.get_y() <= 6:
            self._at_bottom = True

    def randomize(self):
        """Randomizes Mineral's attributes.
        
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
            self._text = "#"
            self._value = -1

        # Change color.
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        self._color = Color(r, g, b)

        x = random.randint(1, constants.COLUMNS - 1) * constants.CELL_SIZE
        y = 0
        new_position = Point(x, y)
        self._position = new_position

    def get_at_bottom(self):
        """Returns whether the mineral is at the bottom of the screen
        as a bool.
        """
        return self._at_bottom

    def get_value(self):
        """Returns point value of the mineral.
        Args:
            self (Mineral): an instance of Mineral
        """
        return self._value