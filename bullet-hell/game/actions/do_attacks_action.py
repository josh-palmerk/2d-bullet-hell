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
            self.do_attack_1(player, cast)
        
        for attacker in enemies:
            if isinstance(attacker, Dummy): #dummy should target just one consistent direction
                attacker.set_target(Point(attacker.get_position().get_x() + 5, attacker.get_position().get_y()))
            else:
                attacker.set_target(player.get_center_position()) 
            attacker.roll_attack_chance_1() 
            if self.determine_attack_1(attacker):
                self.do_attack_1(attacker, cast)
            

    def determine_attack_1(self, attacker):
            if attacker.is_attacking_1() and attacker.get_attack_1() is not None:
                return True
            else:
                return False

    def do_attack_1(self, attacker, cast):
        attack_1 = attacker.get_attack_1()
        attack_1.spawn_attack(cast, attacker)
        attacker.set_is_attacking_1(False)
