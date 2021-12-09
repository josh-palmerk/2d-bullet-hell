from game.actions.action import Action
from game.point import Point
from game import game_balance as gb

class HandleWallsAction(Action):
    def __init__(self, physics_service) -> None:
        super().__init__()
        self._physics_service = physics_service

    def execute(self, cast):
        player = cast["player"][0]
        enemies = cast["enemies"]
        bullets = cast["bullets"]
        walls = cast["walls"]

        for wall in walls:
            if self._physics_service.is_collision(wall, player):
                short_side = self._physics_service.short_collision_side(player, wall)
                if wall.get_position().get_quadrant(player.get_position()) != 1:
                    short_side = short_side.reverse()
                
                new_pos = player.get_position().add(short_side)#.scale(100))
                player.set_position(new_pos)


            for enemy in enemies:

                if self._physics_service.is_collision(wall, enemy):
                    short_side = self._physics_service.short_collision_side(wall, enemy)
                    if wall.get_position().get_quadrant(enemy.get_position()) != 1:
                        short_side = short_side.reverse()
                    
                    new_pos = enemy.get_position().add(short_side)#.scale(100))
                    enemy.set_position(new_pos)
                
                if self._physics_service.is_collision(enemy, player):
                    short_side = self._physics_service.short_collision_side(enemy, player)
                    if enemy.get_position().get_quadrant(player.get_position()) != 1:
                        short_side = short_side.reverse()
                    
                    new_pos = player.get_position().add(short_side.scale(gb.ENEMY_KNOCKBACK))
                    player.add_health(-gb.KNOCKBACK_DAMAGE)
                    cast["UI"][0].set_text(str(player.get_health()))

                    player.set_position(new_pos)
