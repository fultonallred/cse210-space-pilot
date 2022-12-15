from game.scripting.action import Action
from game.casting.asteroid import Asteroid
from game.casting.mineral import Mineral

class AddEnemiesAction(Action):
    """AddEnemiesAction is responsible for adding more enemies to the game at
    certain frame increments.
    
    Attributes:
        None
    """

    def execute(self, cast, script):
        """Checks if game is ready to add more enemies and calls methods
        to add them.
        
        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        is_game_over = script.get_actions("update")[3].get_game_over()

        if not is_game_over:
            frame_counter = cast.get_first_actor("frame_counter")
            frames = frame_counter.get_frames()

            if frames % 360 == 0:
                self._add_asteroid(cast)

            if frames % 36 == 0:
                self._add_mineral(cast)

    def _add_asteroid(self, cast):
        """Create an additional asteroid."""
        asteroid = Asteroid()
        cast.add_actor("asteroids", asteroid)

    def _add_mineral(self, cast):
        """Create and additional mineral."""
        mineral = Mineral()
        cast.add_actor("minerals", mineral)