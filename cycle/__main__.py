from game.casting.cast import Cast
from game.casting.powerup import Powerup
from game.casting.frame_counter import FrameCounter
from game.casting.health_display import HealthDisplay
from game.casting.space_ship import Spaceship
from game.casting.mineral import Mineral

from game.scripting.add_enemies_action import AddEnemiesAction
from game.scripting.control_spaceship_action import ControlSpaceshipAction
from game.directing.director import Director
from game.scripting.draw_actors_action import DrawActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.services.keyboard_service import KeyboardService
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.script import Script
from game.scripting.update_hud_action import UpdateHUD
from game.services.video_service import VideoService

def main():
    
    # Create the starting cast.
    cast = Cast()
    cast.add_actor("pickups", Powerup())
    cast.add_actor("ships", Spaceship())
    cast.add_actor("displays", HealthDisplay())
    cast.add_actor("frame_counter", FrameCounter())
    cast.add_actor("minerals", Mineral())
  
    # Start the game.
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlSpaceshipAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", UpdateHUD())
    script.add_action("update", AddEnemiesAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()