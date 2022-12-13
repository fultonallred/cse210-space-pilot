from game.scripting.action import Action

class UpdateHUD(Action):
    """Updates the health and points on the scoreboard."""


    def execute(self, cast, script):
        spaceship = cast.get_first_actor("ships")
        power = spaceship.get_power()
        health = spaceship.get_health()

        health_display = cast.get_first_actor("displays")
        health_display.set_text(f"Health: {health}, Power: {power}")