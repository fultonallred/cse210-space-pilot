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
        
        self._video_service.clear_buffer()
        
        self._draw_spaceship(cast, script)
        self._draw_asteroids(cast, script)
        self._draw_hud(cast, script)
        self._draw_others(cast, script)
      
        self._video_service.flush_buffer()

    def _draw_asteroids(self, cast, script):
        """This draws all asteroids and lasers."""

        asteroids = cast.get_actors("asteroids")
        asteroid_segments = []
        asteroid_lasers = []
        
        for asteroid in asteroids:
            segments = asteroid.get_segments()
            lasers = asteroid.get_lasers()
            asteroid_segments.extend(segments)
            asteroid_lasers.extend(lasers)
        
        self._video_service.draw_actors(asteroid_segments)
        self._video_service.draw_actors(asteroid_lasers)

    def _draw_spaceship(self, cast, script):
        """Draws the player's ship and lasers."""

        spaceship = cast.get_first_actor("ships")
        spaceship_segments = spaceship.get_segments()
        spaceship_lasers = spaceship.get_lasers()

        self._video_service.draw_actors(spaceship_segments)
        self._video_service.draw_actors(spaceship_lasers)

    def _draw_hud(self, cast, script):
        """This draws all elements of the heads-up-display."""

        messages = cast.get_actors("messages")
        self._video_service.draw_actors(messages, True)

        health_display = cast.get_first_actor("displays")
        self._video_service.draw_actor(health_display)


    def _draw_others(self, cast, script):
        """Draws all other actors without dedicated methods."""

        food = cast.get_first_actor("foods")
        self._video_service.draw_actor(food)

        minerals = cast.get_actors("minerals")
        self._video_service.draw_actors(minerals)