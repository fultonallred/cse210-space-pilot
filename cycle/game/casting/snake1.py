from game.casting.snake import Snake
import constants
from game.shared.point import Point
from game.casting.actor import Actor

class Snake1(Snake):
    """Snake1 is for player 1. It has a different starting position than
    Snake.
    """
    
    def grow_tail(self, number_of_segments):
        """Grows tail by segments equal to the point value of food consumed.
        """
        
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            segment.set_color(constants.RED)
            self._segments.append(segment)

    def _prepare_body(self):
        """This method is overridden from Snake to change starting position.
        """
        x = int(constants.MAX_X / 2 + 300)
        y = int(constants.MAX_Y / 2)

        for i in range(constants.SNAKE_LENGTH):
            position = Point(x , y + i * constants.CELL_SIZE)
            velocity = Point(0, -1 * constants.CELL_SIZE)
            text = "8" if i == 0 else "#"
            color = constants.RED
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)