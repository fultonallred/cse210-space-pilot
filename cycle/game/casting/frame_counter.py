from game.casting.actor import Actor
import constants

class FrameCounter(Actor):
    """Frame counter counts the amount of frames since start of game."""

    def __init__(self):
        """Constructs a new instance of FrameCounter.
        
        Attributes:
            frames (int): number of frames counted
            frame_rate (int): number of frames per second
            """

        self._frames = 0
        self._frame_rate = constants.FRAME_RATE

    def move_next(self):
        """Responsible for increasing the frame count."""
        self._frames += 1
        if self._frames == self._frame_rate * 1000:
            self._frames = 0

        self._level = self._frames
        
    def get_frames(self):
        """Return the current frame count."""

        return self._frames