from game.actions.action import Action
from game.enemies.dummy import Dummy
from game.point import Point

class DoAttacksAction(Action):
    def __init__(self) -> None:
        super().__init__()

    def execute(self, cast):
        player = cast["player"][0]
        enemies = cast["enemies"]

        if self.determine_attack_1(player):
            player.get_attack_1().update(cast, player)
        for enemy in enemies:

            if isinstance(enemy, Dummy): #dummy should target just one consistent direction
                    enemy.set_target(Point(enemy.get_position().get_x() + 5, enemy.get_position().get_y()))
            else:
                enemy.set_target(player.get_center_position()) 

            if self.determine_attack_1(enemy):
                enemy.roll_attack_chance_1()
                enemy.get_attack_1().update(cast, enemy)

        # if self.determine_attack_1(player):
        #     self.do_attack_1(player, cast)
        
        # for attacker in enemies:
        #     if isinstance(attacker, Dummy): #dummy should target just one consistent direction
        #         attacker.set_target(Point(attacker.get_position().get_x() + 5, attacker.get_position().get_y()))
        #     else:
        #         attacker.set_target(player.get_center_position()) 
        #     if not attacker.is_attacking_1():
        #         attacker.roll_attack_chance_1() 
        #     if self.determine_attack_1(attacker):
        #         self.do_attack_1(attacker, cast)
            

    def determine_attack_1(self, attacker):
            if attacker.get_attack_1() is not None:
                return True
            else:
                return False

    def do_attack_1(self, attacker, cast):
        attack_1 = attacker.get_attack_1()
        attacker.set_is_attacking_1(attack_1.update(cast, attacker)
)
