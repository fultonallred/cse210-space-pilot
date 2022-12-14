import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point
import random

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False


    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """

        # Get spaceship objects
        self._spaceship = cast.get_first_actor("ships")
        self._spaceship_segments = self._spaceship.get_segments()
        self._spaceship_lasers = self._spaceship.get_lasers()

        # Get asteroid objects
        self._asteroids = cast.get_actors("asteroids")
        self._asteroid_segments = []
        self._asteroid_lasers = []
        for asteroid in self._asteroids:
            self._asteroid_segments.extend(asteroid.get_segments())
            self._asteroid_lasers.extend(asteroid.get_lasers())

        self._minerals = cast.get_actors("minerals")

        self._food = cast.get_first_actor("foods")

        if not self._is_game_over:
            self._handle_food_collision(cast)
        #     self._handle_segment_collision(cast)
            self._handle_mineral_collision(cast)
            self._handle_laser_collision(cast)
            self.check_game_over(cast)
            self._handle_game_over(cast)

    def _handle_food_collision(self, cast):
        """Updates the score and moves the food if the snake collides with the food.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        food = cast.get_first_actor("foods")
        ship = cast.get_first_actor("ships")
        ship_segments = ship.get_segments()


        for segment in ship_segments:
            if food.get_position().equals(segment.get_position()):
                ship.activate_power()
                print(ship.get_power())
                food.reset()

    def _handle_mineral_collision(self, cast):
        """Decreases player health if they collide with a mineral."""

        spaceship = cast.get_first_actor("ships")
        segments = spaceship.get_segments()
        minerals = cast.get_actors("minerals")
        
        for mineral in minerals:
            for segment in segments:
                if mineral.get_position().is_close(segment.get_position()):
                    spaceship.add_health(-1)
                    mineral.randomize()
                """"""
    
    def _handle_laser_collision(self, cast):
        """"""
        asteroid = cast.get_first_actor("asteroids")
        asteroid_segments = asteroid.get_segments()
        asteroid_lasers = asteroid.get_lasers()

        spaceship = cast.get_first_actor("ships")
        spaceship_segments = spaceship.get_segments()
        spaceship_lasers = spaceship.get_lasers()

        minerals = cast.get_actors("minerals")

        # Handle spaceship lasers.
        for mineral in minerals:
            for laser in spaceship_lasers:
                if mineral.get_position().is_close(laser.get_position()):
                    print("Laser hits")
                    mineral.randomize()
                    spaceship.remove_laser(laser)
                    spaceship.add_mineral_destroyed()

        for segment in asteroid_segments:
            for laser in spaceship_lasers:
                if segment.get_position().is_close(laser.get_position()):
                    asteroid.add_damage(1)
                    spaceship.remove_laser(laser)

        # Handle asteroid lasers.
        for segment in spaceship_segments:
            for laser in asteroid_lasers:
                if segment.get_position().is_close(laser.get_position()):
                    spaceship.add_health(-1)
                    print("Spaceship hit")
                    asteroid.remove_laser(laser)
                    if spaceship.get_health() <= 0:
                        self._is_game_over = True

    def check_game_over(self, cast):
        """Checks if there is a game over."""
        spaceship = cast.get_first_actor("ships")
        if spaceship.get_health() <= 0:
            self._is_game_over = True
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:

            asteroid = cast.get_first_actor("asteroids")
            asteroid_segments = asteroid.get_segments()
            asteroid_lasers = asteroid.get_lasers()

            spaceship = cast.get_first_actor("ships")
            spaceship_segments = spaceship.get_segments()
            spaceship_lasers = spaceship.get_lasers()
            health_display = cast.get_first_actor("displays")

            actors = cast.get_all_actors()
            actors.extend(asteroid_segments)
            actors.extend(asteroid_lasers)
            actors.extend(spaceship_segments)
            actors.extend(spaceship_lasers)
            actors.append(health_display)

            for actor in actors:
                actor.set_color(constants.WHITE)

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

    def get_game_over(self):
        """Returns if the game is over or not.
        
        Return:
            Bool: if game is over or not.
        """
        return self._is_game_over
