import constants
import random
from game.shared.point import Point
from game.casting.actor import Actor

class Spaceship(Actor):

    def __init__(self):
        super().__init__()
        """
        """

        self._segments = []
        self._lasers = []
        self._firing = False
        self._cooldown = 0
        self._prepare_body()

    def _prepare_body(self):
        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y / 2)

        # Prepare head
        self._prepare_segment(Point(x, y), Point(0, 0), "#", constants.GREEN)

        # Prepare body
        self._prepare_segment(Point(x, y + constants.CELL_SIZE), 
        Point(0, 0), "#", constants.GREEN)

        # Prepare left wing
        self._prepare_segment(Point(x - constants.CELL_SIZE,
        y + constants.CELL_SIZE), Point(0, 0), "<", constants.GREEN)

        # Prepare right wing
        self._prepare_segment(Point(x + constants.CELL_SIZE, y + constants.CELL_SIZE), 
        Point(0, 0), ">", constants.GREEN)


    def _prepare_segment(self, position, velocity, text, color):
        """Creates the spaceship in the middle of the screen."""

        segment = Actor()
        segment.set_position(position)
        segment.set_velocity(velocity)
        segment.set_text(text)
        segment.set_color(color)
        self._segments.append(segment)

    def get_segments(self):
        """Returns each segment of the Spaceship in a list.
        """
        return self._segments

    def move_next(self):
        for segment in self._segments:
            segment.set_velocity(self._velocity)
            segment.move_next()
        for laser in self._lasers:
            laser.move_next()
            position = laser.get_position()
            y_position = position.get_y()
            if y_position == constants.MAX_Y - 15:
                self._lasers.remove(laser)
        
        self._cooldown -= 1
        if self._cooldown < 0: self._cooldown = 0


    def fire_laser(self):
        """Fires a laser."""

        if self._cooldown <= 0:
            head = self._segments[0]
            laser = Actor()
            laser.set_position(head.get_position())
            laser.set_velocity(Point(0, -1 * constants.CELL_SIZE))
            laser.set_text("|")
            laser.set_color(constants.RED)
            self._lasers.append(laser)
            self._cooldown = 3

    def get_lasers(self):
        return self._lasers

    def remove_laser(self, laser):
        self._lasers.remove(laser)