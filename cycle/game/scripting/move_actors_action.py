from game.scripting.action import Action


# TODO: Implement MoveActorsAction class here! 

# Override the execute(cast, script) method as follows:
# 1) get all the actors from the cast
# 2) loop through the actors
# 3) call the move_next() method on each actor

class MoveActorsAction(Action):
    """Moves each actor to the next position.
    
    Attributes: none
    """

    def execute(self, cast, script):
        """Gets all actors and tells them to move to their next position.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """

        actors = cast.get_all_actors()
        for actor in actors:
            actor.move_next()