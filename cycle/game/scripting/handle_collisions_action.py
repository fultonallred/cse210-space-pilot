import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

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
        # if not self._is_game_over:
        #     self._handle_food_collision(cast)
        #     self._handle_segment_collision(cast)
        #     self._handle_game_over(cast)

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
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        # if self._is_game_over:

        #     snake0 = cast.get_actor("snakes", 0)
        #     snake1 = cast.get_actor("snakes", 1)
        #     segments0 = snake0.get_segments()
        #     segments1 = snake1.get_segments()
        #     segments = segments0 + segments1
        #     food = cast.get_first_actor("foods")

        #     x = int(constants.MAX_X / 2)
        #     y = int(constants.MAX_Y / 2)
        #     position = Point(x, y)

        #     message = Actor()
        #     message.set_text("Game Over!")
        #     message.set_position(position)
        #     cast.add_actor("messages", message)

        #     for segment in segments:
        #         segment.set_color(constants.WHITE)
        #     food.set_color(constants.WHITE)

    def get_game_over(self):
        """Returns if the game is over or not.
        
        Return:
            Bool: if game is over or not.
        """
        return self._is_game_over
