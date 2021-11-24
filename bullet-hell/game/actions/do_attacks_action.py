from game.actions.action import Action

class DoAttacksAction(Action):
    def __init__(self) -> None:
        super().__init__()

    def execute(self, cast):
        player = cast["player"][0]
        enemies = cast["enemies"]
        attackers = enemies       # <-- redundant???
        attackers.append(player)
        for attacker in attackers:
            if attacker.is_attacking_1():
                if attacker.get_attack_1() is not None:
                    attack_1 = attacker.get_attack_1()
                    attack_1.spawn_attack(cast, attacker.get_target(), attacker.get_bullet_speed(), attacker.get_position())
                    attacker.set_is_attacking_1(False)
