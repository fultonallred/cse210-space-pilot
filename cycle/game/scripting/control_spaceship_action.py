import constants
from game.scripting.action import Action
from game.shared.point import Point
from game.casting.actor import Actor


class ControlSpaceshipAction(Action):
    """
    An input action that controls the spaceship.
    
    The responsibility of ControlSpaceshipAction is to get the direction and move the spaceship.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlSpaceshipAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction = Point(0, 0)

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        spaceship = cast.get_first_actor("ships")

        # remain still
        dx = 0
        dy = 0

        # left
        if self._keyboard_service.is_key_down('A'):
            dx = -1
        
        # right
        if self._keyboard_service.is_key_down('D'):
            dx = 1
        # up
        if self._keyboard_service.is_key_down('W'):
            dy = -1
        # down
        if self._keyboard_service.is_key_down('S'):
            dy = 1

        if self._keyboard_service.is_key_down('space'):
            spaceship.fire_laser()
            

        self._direction = Point(dx, dy)
        self._direction = self._direction.scale(constants.CELL_SIZE)
        spaceship.set_velocity(self._direction)
        
