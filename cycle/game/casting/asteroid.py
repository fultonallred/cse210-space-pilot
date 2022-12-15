from game.casting.space_ship import Spaceship
import random
import constants
from game.shared.color import Color
from game.shared.point import Point
from game.casting.actor import Actor


class Asteroid(Spaceship):
    """Asteroid moves from the top to bottom of the screen and must be shot
    multiple times to be destroyed."""
    
    def __init__(self):
        super().__init__()

        speed = random.randint(1, 5)
        self._velocity = Point(0, speed)
        self._health = 10

    def _prepare_body(self):
        """Creates the body segments of Asteroid, called through parent
        constructor."""
        
        x = random.randint(1, constants.COLUMNS - 2) * constants.CELL_SIZE
        y = -30

        # Prepare head
        self._prepare_segment(Point(x, y), Point(0, 0), "0", constants.GREEN)

        # Prepare body
        self._prepare_segment(Point(x, y + constants.CELL_SIZE), 
        Point(0, 0), "0", constants.GREEN)

        # Prepare left wing
        self._prepare_segment(Point(x + constants.CELL_SIZE,
        y + constants.CELL_SIZE), Point(0, 0), "0", constants.GREEN)

        # Prepare right wing
        self._prepare_segment(Point(x + constants.CELL_SIZE, y), 
        Point(0, 0), "0", constants.GREEN)

    def move_next(self):
        """Handles the movement of each segment and laser."""
        for segment in self._segments:
            segment.set_velocity(self._velocity)
            segment.move_next()

        # trigger = random.randint(1, 20)
        
        # if trigger == 1:
        #     self.fire_laser()

        for laser in self._lasers:
            laser.move_next()
            position = laser.get_position()
            y_position = position.get_y()
            if y_position == constants.MAX_Y:
                self._lasers.remove(laser)

    def fire_laser(self):
        """Creates a new laser object."""
        head = self._segments[2]
        laser = Actor()
        laser.set_position(head.get_position())
        laser.set_velocity(Point(0, 15))
        laser.set_text("|")
        laser.set_color(constants.RED)
        self._lasers.append(laser)

    def reset(self):
        """Resets the asteroid."""
        self._segments = []
        self._health = 10
        self._prepare_body()
        speed = random.randint(1, 5)
        self._velocity = Point(0, speed)

    def add_damage(self, amount):
        """Decreases health by given amount."""
        self._health -= amount