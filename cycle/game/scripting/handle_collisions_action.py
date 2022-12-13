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
        self._handle_game_over(cast)
        if not self._is_game_over:
        #     self._handle_food_collision(cast)
        #     self._handle_segment_collision(cast)
            self._handle_mineral_collision(cast)
            self._handle_laser_collision(cast)

    # def _handle_food_collision(self, cast):
    #     """Updates the score nd moves the food if the snake collides with the food.
        
    #     Args:
    #         cast (Cast): The cast of Actors in the game.
    #     """
    #     food = cast.get_first_actor("foods")
    #     snakes = cast.get_actors("snakes")
    #     snake0 = snakes[0]
    #     snake1 = snakes[1]
    #     head0 = snake0.get_head()
    #     head1 = snake1.get_head()
    #     scores = cast.get_actors("scores")
    #     foods = cast.get_actors("foods")

    #     for food in foods:
    #         if head0.get_position().equals(food.get_position()):
    #             points = food.get_points()
    #             snake0.grow_tail(points)
    #             scores[0].add_points(points)
    #             print(scores[0])
    #             food.reset()

    #         elif head1.get_position().equals(food.get_position()):
    #             points = food.get_points()
    #             snake1.grow_tail(points)
    #             scores[1].add_points(points)
    #             food.reset()
    
    # def _handle_segment_collision(self, cast):
    #     """Sets the game over flag if the snake collides with one of its segments.
        
    #     Args:
    #         cast (Cast): The cast of Actors in the game.
    #     """
    #     snake0 = cast.get_actor("snakes", 0)
    #     snake1 = cast.get_actor("snakes", 1)

    #     head0 = snake0.get_segments()[0]
    #     head1 = snake1.get_segments()[0]

    #     segments0 = snake0.get_segments()[1:]
    #     segments1 = snake1.get_segments()[1:]

    #     segments = segments0 + segments1
    #     for segment in segments:
    #         if head0.get_position().equals(segment.get_position()):
    #             self._is_game_over = True
    #         elif head1.get_position().equals(segment.get_position()):
    #             self._is_game_over = True

    def _handle_mineral_collision(self, cast):
        spaceship = cast.get_first_actor("ships")
        segments = spaceship.get_segments()
        body = segments[1]

        body_position = body.get_position()
        minerals = cast.get_actors("minerals")
        
        for mineral in minerals:
            mineral_position = mineral.get_position()
            if body_position.equals(mineral_position):
                """"""
    
    def _handle_laser_collision(self, cast):
        """"""
        asteroid = cast.get_first_actor("asteroids")
        asteroid_segments = asteroid.get_segments()
        asteroid_lasers = asteroid.get_lasers()

        spaceship = cast.get_first_actor("ships")
        spaceship_segments = spaceship.get_segments()
        spaceship_lasers = spaceship.get_lasers()
        health_display = cast.get_first_actor("displays")

        minerals = cast.get_actors("minerals")

        # Handle spaceship lasers.
        for mineral in minerals:
            for laser in spaceship_lasers:
                if mineral.get_position().is_close(laser.get_position()):
                    print("Laser hits")
                    mineral.randomize()
                    spaceship.remove_laser(laser)

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
                    health_display.set_text(f"Health: {spaceship.get_health()}")
                    print("Spaceship hit")
                    asteroid.remove_laser(laser)
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
