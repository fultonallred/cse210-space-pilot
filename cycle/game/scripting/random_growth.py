import constants
import random
from game.scripting.action import Action


class RandomGrowth(Action):
    """Thie responsibility of RandomGrowth is to give a chance for each snake
    to grow.
    """

    def __init__(self):
        self._frame_rate = constants.FRAME_RATE

    def execute(self, cast, script):
        """Picks a random number, if it is 1, grow will be true.

        Return:
            Bool
        """
        update_actions = script.get_actions("update")
        if not update_actions[1].get_game_over():
            int = random.randint(1, self._frame_rate * 2)
            snakes = cast.get_actors("snakes")

            if int == 1:
                for snake in snakes:
                    snake.grow_tail(1)