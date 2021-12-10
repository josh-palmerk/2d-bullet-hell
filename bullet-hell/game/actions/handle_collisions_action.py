from random import randint
from game import constants
from game.actions.action import Action
from game.point import Point
from game.services.audio_service import AudioService

# TODO: everything lmao

class HandleCollisionsAction(Action):
    """
    Child of Action that handles collision for all actors in the game. Just call execute(cast).
    """
    def __init__(self, physics_service) -> None:
        super().__init__()
        self._physics_service = physics_service
        self._audio_service = AudioService()

    def execute(self, cast):
        """ deez nuts """
        player = cast["player"][0]
        enemies = cast["enemies"]
        bullets = cast["bullets"]
        walls = cast["walls"]

        q = 0
        for bullet in bullets:
            if bullet.hurts_player():
                if self._physics_service.is_collision(player, bullet):
                    if not player.is_invincible():
                        player.add_health(-bullet.get_damage())
                    cast["UI"][0].set_text(str(player.get_health()))

                    # TODO add effects here like I frames or other things to trigger on hit
                    if not player.is_dodging():
                        cast["bullets"].pop(q)
                        q -= 1
                    

            if bullet.hurts_enemies():
                for enemy in enemies:
                    if self._physics_service.is_collision(enemy, bullet):
                        if not enemy.is_invincible():
                            enemy.add_health(-bullet.get_damage())

                        # TODO add other things here on enemy hit

                        # if bullet has pierce dont pop it?? potential feature. would need to be "off" for a little bit tho
                        # for one-hit validation with pierce and such you would need to have every bullet have a list of what it's hit
                        if bullet in cast["bullets"]:
                            cast["bullets"].pop(q)
                            q -= 1

                
                    if enemy.get_health() <= 0:
                        cast["enemies"].remove(enemy)
                        continue
            
            for wall in walls:
                if self._physics_service.is_collision(wall, bullet):
                    cast["bullets"].pop(q)
                    q -= 1
            
            if bullet.get_range() <= 0:
                cast["bullets"].pop(q)
                q -= 1

            q += 1
