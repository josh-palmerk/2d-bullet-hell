from game.actions.action import Action

class UpdateMovementsAction(Action):
    """ Updates velocities based on movement patterns. Mostly for enemies I think?? """
    def __init__(self) -> None:
        super().__init__()

    def execute(self, cast):
        for enemy in cast["enemies"]:
            enemy.do_movement_pattern()
