from game.scripting.action import Action

class UpdateHUD(Action):
    """UpdateHUD is repsponsible for updating items on the HUD.
    
    Attributes:
        None
    """
    
    def execute(self, cast, script):
        """Gets elements of the HUD and set their information to something new.
        
        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        spaceship = cast.get_first_actor("ships")
        power = spaceship.get_power()
        health = spaceship.get_health()

        health_display = cast.get_first_actor("displays")
        health_display.set_text(f"Health: {health}, Power: {power}")