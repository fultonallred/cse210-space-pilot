from game.scripting.action import Action


class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        scores = cast.get_actors("scores")
        score0 = scores[0]
        score1 = scores[1]
        foods = cast.get_actors("foods")
        food0 = foods[0]
        food1 = foods[1]
        snakes = cast.get_actors("snakes")
        segments0 = snakes[0].get_segments()
        segments1 = snakes[1].get_segments()
        messages = cast.get_actors("messages")

        self._video_service.clear_buffer()
        self._video_service.draw_actor(food0)
        self._video_service.draw_actor(food1)
        self._video_service.draw_actors(segments0)
        self._video_service.draw_actors(segments1)
        self._video_service.draw_actor(score0)
        self._video_service.draw_actor(score1, True)
        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()