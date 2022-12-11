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
            """
        self._mineral_type = ""
        self._value = 1
        self.prepare_mineral()

    def get_value(self):
        """Returns point value of the mineral.
        Args:
            self (Mineral): an instance of Mineral
        """
        return self._value

    def prepare_mineral(self):

        speed = random.randint(1, 5)
        mineral_velocity = Point(0, speed)
        
        x = random.randint(1, constants.COLUMNS - 1)
        y = random.randint(1, constants.ROWS - 1)
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

        x = (self._position.get_x() + self._velocity.get_x()) % constants.MAX_X
        y = (self._position.get_y() + self._velocity.get_y()) % constants.MAX_Y
        self._position = Point(x, y)
        
        if 600 - self._position.get_y() <= 1:
            self.randomize()

    def randomize(self):
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
            self._text = "#"
            self._value = -1

        # Change color.
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        self._color = Color(r, g, b)

        x = random.randint(1, 59) * 15
        y = -30
        new_position = Point(x, y)
        self._position = new_position