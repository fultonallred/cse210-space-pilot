import random
from game.scripting.action import Action
from game.casting.asteroid import Asteroid
from game.casting.mineral import Mineral

class AddEnemiesAction(Action):
    """AddEnemiesAction is responsible for adding more enemies to the game at
    certain frame increments.
    
    Attributes:
        None
    """
    def __init__(self):
        """Constructs a new instance of AddEnemiesAction."""
        self._mineral_increase = 1

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
            spaceship = cast.get_first_actor("ships")
            minerals_destroyed = spaceship.get_minerals_destroyed()
            if minerals_destroyed > 998:
                minerals_destroyed = 998

            # A new asteroid is added every 360 frames. The chance for extras
            # to spawn increases with each asteroid destroyed.
            asteroids_destroyed = spaceship.get_asteroids_destroyed()
            if asteroids_destroyed > 98:
                asteroids_destroyed = 98
            new_asteroid = random.randint(1, 360 - asteroids_destroyed) == 1
            if frames % 360 == 0 or new_asteroid:
                self._add_asteroid(cast)

            # Minerals are added every 36 frames. The amount added has a
            # greater chance to increase with every mineral destroyed.
            if random.randint(1, 1000 - minerals_destroyed) == 1:
                self._mineral_increase += 1
            if frames % 36 == 0:
                for n in range(self._mineral_increase):
                    self._add_mineral(cast)

    def _add_asteroid(self, cast):
        """Create an additional asteroid."""
        asteroid = Asteroid()
        cast.add_actor("asteroids", asteroid)

    def _add_mineral(self, cast):
        """Create and additional mineral."""
        mineral = Mineral()
        cast.add_actor("minerals", mineral)