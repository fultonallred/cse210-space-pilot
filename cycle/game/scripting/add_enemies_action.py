from game.scripting.action import Action
from game.casting.asteroid import Asteroid
from game.casting.mineral import Mineral

class AddEnemiesAction(Action):
    """AddEnemiesAction is responsible for adding more enemies to the game at
    certain frame increments."""

    def execute(self, cast, script):
        """Checks if game is ready to add more enemies."""

        frame_counter = cast.get_first_actor("frame_counter")
        frames = frame_counter.get_frames()

        if frames % 360 == 0:
            self._add_asteroid(cast)

        if frames % 36 == 0:
            self._add_mineral(cast)

    def _add_asteroid(self, cast):
        """This method will create an additional asteroid."""
        asteroid = Asteroid()
        cast.add_actor("asteroids", asteroid)

    def _add_mineral(self, cast):
        """This will add a mineral."""
        mineral = Mineral()
        cast.add_actor("minerals", mineral)