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
        #scores = cast.get_actors("scores")
        health_display = cast.get_first_actor("displays")
        #score1 = scores[1]
        minerals = cast.get_actors("minerals")
        #foods = cast.get_actors("foods")
        #food0 = foods[0]
        #food1 = foods[1]
        #snakes = cast.get_actors("snakes")
        #segments0 = snakes[0].get_segments()
        #segments1 = snakes[1].get_segments()
        spaceship = cast.get_first_actor("ships")
        spaceship_segments = spaceship.get_segments()
        ship_lasers = spaceship.get_lasers()
        asteroid = cast.get_first_actor("asteroids")
        asteroid_segments = asteroid.get_segments()
        asteroid_lasers = asteroid.get_lasers()
        messages = cast.get_actors("messages")

        self._video_service.clear_buffer()
        self._video_service.draw_actors(minerals)
        #self._video_service.draw_actor(food0)
        #self._video_service.draw_actor(food1)
        self._video_service.draw_actors(spaceship_segments)
        self._video_service.draw_actors(ship_lasers)
        self._video_service.draw_actors(asteroid_segments)
        self._video_service.draw_actors(asteroid_lasers)

        #self._video_service.draw_actors(segments0)
        #self._video_service.draw_actors(segments1)
        self._video_service.draw_actor(health_display)
        #self._video_service.draw_actor(score1, True)
        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()