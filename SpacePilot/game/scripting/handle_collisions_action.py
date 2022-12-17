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
        self._removed = 0


    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        self._spaceship = cast.get_first_actor("ships")
        self._spaceship_segments = self._spaceship.get_segments()
        self._spaceship_lasers = self._spaceship.get_lasers()
        self._asteroids = cast.get_actors("asteroids")
        self._minerals = cast.get_actors("minerals")
        self._powerup = cast.get_first_actor("pickups")
        self._health_display = cast.get_first_actor("displays")

        if not self._is_game_over:
            self._handle_food_collision(cast)
            self._handle_mineral_collision(cast)
            self._handle_laser_collision(cast)
            self._check_game_over(cast)
            self._handle_game_over(cast)

    def _handle_food_collision(self, cast):
        """Updates the score and moves the food if the player collides with it.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """

        for segment in self._spaceship_segments:
            if self._powerup.get_position().equals(segment.get_position()):
                self._spaceship.activate_power()
                self._powerup.reset()

    def _handle_mineral_collision(self, cast):
        """Decreases player health if they collide with a mineral. Removes
        mineral upon player contact or contact with bottom of screen.
        """

        for mineral in self._minerals:
            if mineral.get_at_bottom():
                cast.remove_actor("minerals", mineral)
            else:
                for segment in self._spaceship_segments:
                    if mineral.get_position().is_close(segment.get_position()):
                        self._spaceship.add_health(-1)
                        cast.remove_actor("minerals", mineral)
                        mineral.randomize()
    
    def _handle_laser_collision(self, cast):
        """"""

        # Handle spaceship-mineral contact.
        for mineral in self._minerals:
            remove = False
            for laser in self._spaceship_lasers:
                if mineral.get_position().is_close(laser.get_position()):
                    remove = True
                    self._spaceship.remove_laser(laser)
                    self._spaceship.add_mineral_destroyed()
            if remove:
                    cast.remove_actor("minerals", mineral)

        # Handle asteroid-spaceship contact.
        for asteroid in self._asteroids:
            segments = asteroid.get_segments()

            for segment in segments:

                for ship_segment in self._spaceship_segments:
                    if segment.get_position().is_close(ship_segment.get_position()):
                        self._spaceship.add_health(-1)

                for laser in self._spaceship_lasers:
                    remove_laser = False
                    if segment.get_position().is_close(laser.get_position()):
                        asteroid.add_damage(1)
                        remove_laser = True
                    if remove_laser:
                        self._spaceship.remove_laser(laser)

            if asteroid.get_health() <= 0:
                cast.remove_actor("asteroids", asteroid)
                self._spaceship.add_asteroid_destroyed()
                print(self._spaceship.get_asteroids_destroyed())

            for laser in asteroid.get_lasers():
                remove_laser = False

                for segment in self._spaceship_segments:
                    if segment.get_position().is_close(laser.get_position()):
                        self._spaceship.add_health(-1)
                        remove = True

                if remove_laser:
                    asteroid.remove_laser(laser)
                    

    def _check_game_over(self, cast):
        """Checks if there is a game over."""
        if self._spaceship.get_health() <= 0:
            self._is_game_over = True
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:


            health_display = cast.get_actors("displays")
            asteroid_segments = []
            for asteroid in self._asteroids:
                asteroid_segments.extend(asteroid.get_segments())

            actors = cast.get_all_actors()
            actors.extend(asteroid_segments)
            actors.extend(self._spaceship_segments)
            actors.extend(self._spaceship_lasers)
            actors.extend(health_display)

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
