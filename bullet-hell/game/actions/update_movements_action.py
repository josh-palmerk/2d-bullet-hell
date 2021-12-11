from game.actions.action import Action

class UpdateMovementsAction(Action):
    """ Updates velocities based on movement patterns. Mostly for enemies I think?? """
    def __init__(self) -> None:
        super().__init__()

    def execute(self, cast):
        
        player = cast["player"][0]
        if player.is_motioning_1() and player.get_motion_1() is not None:
            player.get_motion_1().update()

        for enemy in cast["enemies"]:
            enemy.make_decisions(player)
