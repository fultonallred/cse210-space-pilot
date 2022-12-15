from game.casting.actor import Actor
import constants

class FrameCounter(Actor):

    def __init__(self):

        self._frames = 0
        self._frame_rate = constants.FRAME_RATE
        self._level = 1

    def move_next(self):

        self._frames += 1
        if self._frames == self._frame_rate * 1000:
            self._frames = 0

        self._level = self._frames
        
    def get_frames(self):

        return self._frames