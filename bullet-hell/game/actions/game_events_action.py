from game.actions.action import Action
from game.director import Director

class GameEventsAction(Action):
    def __init__(self) -> None:
        super().__init__()
        self._director = Director("place", "holders")
    
    def execute(self, cast):
        """Updates the game events that need to occur."""

        # TODO: Add some logic like the following to handle game over conditions
        if cast["player"][0].get_health() <= 0:
            self.game_loss(cast)

        if len(cast["enemies"]) == 0:
            self.game_win(cast)


    def game_win(self, cast):
        """ Called when the game is 'won' """
        print("You cleared all the enemies!\nYou win!!")
        self.end_game(cast)

    def game_loss(self, cast):
        """ Called when the game is 'lost' """
        print("You ran out of health!\nGame over!")
        self.end_game(cast)

    def end_game(self, cast):
        """ Closes the game. """
        cast["keep_playing"][0].increment_counter(-1)