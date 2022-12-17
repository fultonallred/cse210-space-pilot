import constants
import random
from game.shared.point import Point
from game.casting.actor import Actor

class Spaceship(Actor):
    """Spaceship is controlled by the player. It can fire lasers if it
    has power. It takes damage upon contact with other objects."""

    def __init__(self):
        super().__init__()
        """Constructs a new instance of Spaceship. 
        
        Attributes:
            segments (list): a list of Actors that comprise Spaceship
            lasers (list): a list of lasers fired by the Spaceship
            health (int): Spaceship's health
            minerals_destroyed (int): how many minerals Spaceship has shot
            asteroids_destroyed (int): how many asteroids Spaceship has destroyed
            fireable (bool): Whether the Spaceship is able to fire a laser
            power_duration (int): How many times Spaceship can fire a laser
            cooldown (int): the current laser cooldown timer being used
            next_cooldown (int): the next cooldown timer to be used
            """

        self._segments = []
        self._lasers = []
        self._health = 10
        self._minerals_destroyed = 0
        self._asteroids_destroyed = 0
        self._fireable = False
        #self._powerup = False
        self._power_duration = 0
        self._cooldown = 0
        self._next_cooldown = 1
        self._at_bottom = False
        
        self._prepare_body()

    def _prepare_body(self):
        # x = int(constants.MAX_X / 2)
        # y = int(constants.MAX_Y / 2)
        x = int(constants.COLUMNS / 2 * constants.CELL_SIZE)
        y = int(constants.ROWS / 2 * constants.CELL_SIZE)

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
        """Moves each segment and laser to their next posiiton."""
        self.check_at_bottom()
        for segment in self._segments:
            segment.set_velocity(self._velocity)
            segment.move_next()
        for laser in self._lasers:
            laser.move_next()
            position = laser.get_position()
            y_position = position.get_y()
            if y_position == constants.MAX_Y - 15:
                self._lasers.remove(laser)

        self._handle_cooldown()

        
    def _handle_cooldown(self):
        """Determines whether laser is ready to fire again."""

        # Code for different cooldown rates with a powerup.
        # if self._powerup:
        #     if self._cooldown > 0 and self._power_duration > 0:
        #         self._cooldown -= 1
        #         self._power_duration -= 1
        #         self._fireable = False

        #     elif self._cooldown == 0 and self._power_duration > 0:
        #         self._power_duration -= 1
        #         self._fireable = True
        #         self._next_cooldown = 0

        #     elif self._power_duration == 0:
        #         self._powerup = False
        #         self._next_cooldown = 10

        # if not self._powerup:

        if self._power_duration > 0 and self._cooldown == 0:
            self._fireable = True
        
        if self._cooldown > 0:
            self._cooldown -= 1





        
    def fire_laser(self):
        """Creates a new laser object at the head of spaceship that travels
        toward the top of the screen."""
    
        if self._fireable:
            self._fireable = False
            self._power_duration -= 1
            self._cooldown = self._next_cooldown
            head = self._segments[0]
            laser = Actor()
            laser.set_position(head.get_position())
            laser.set_velocity(Point(0, -1 * constants.CELL_SIZE))
            laser.set_text("|")
            laser.set_color(constants.RED)
            self._lasers.append(laser)

    def add_health(self, health):
        """Add a given amount of heatlh, positive or negative, to the spacehship."""
        if self._health == 0:
            self._health = 0
        else:
            self._health += health

    def remove_laser(self, laser):
        self._lasers.remove(laser)

    def activate_power(self):
        """Increases power duration."""
        #self._powerup = True
        self._fireable = True
        power_increase = 10 + self._minerals_destroyed
        self._power_duration += power_increase


    def add_mineral_destroyed(self):
        """Increases the count of minerals destroyed by Spaceship."""
        self._minerals_destroyed += 1

    def add_asteroid_destroyed(self):
        """Increases the count of asteroids destroyed."""
        self._asteroids_destroyed += 1

    def check_at_bottom(self):
        ship_bottom = self._segments[1].get_position()
        self._at_bottom = abs(ship_bottom.get_y() + 15 - constants.MAX_Y) <= 15
        
    def get_power(self):
        """Returns power level."""
        return self._power_duration

    def get_lasers(self):
        return self._lasers

    def get_health(self):
        """Returns health of the ship."""
        return self._health

    def get_at_bottom(self):
        return self._at_bottom

    def get_asteroids_destroyed(self):
        """Returns count of asteroids destroyed."""
        return self._asteroids_destroyed
    
    def get_minerals_destroyed(self):
        """Returns count of minerals destroyed."""
        return self._minerals_destroyed


        



        




