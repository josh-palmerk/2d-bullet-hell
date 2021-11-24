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

        q = 0
        for bullet in bullets:
            
            if self._physics_service.is_collision(player, bullet):
                if bullet.hurts_player():
                    player.add_health(-bullet.get_damage())
                    cast["UI"][0].set_text(str(player.get_health()))

                    # TODO add effects here like I frames or other things to trigger on hit

                    cast["bullets"].pop(q)
                    q -= 1
                    

            for enemy in enemies:
                if self._physics_service.is_collision(enemy, bullet):
                    if bullet.hurts_enemies():
                        enemy.add_health(-bullet.get_damage())

                        # TODO add other things here on enemy hit

                        # if bullet has pierce dont pop it?? potential feature. would need to be "off" for a little bit tho
                        # for one-hit validation with pierce and such you would need to have every bullet have a list of what it's hit
                        cast["bullets"].pop(q)
                        q -= 1

            q += 1



        # balls = cast["balls"]
        # paddle = cast["paddle"][0]
        # bricks = cast["bricks"]

        # for ball in balls:
        #     if self._physics_service.is_collision(paddle, ball):
        #         vel = ball.get_velocity()
        #         new_vel = self.bounce_vertical(vel)
        #         ball.set_velocity(new_vel)
        #         self._audio_service.play_sound(constants.SOUND_BOUNCE)
        #     q = 0
        #     for i in range(len(bricks)):
        #         brick = bricks[q]
        #         if self._physics_service.is_collision(ball, brick):
        #             vel = ball.get_velocity()
        #             new_vel = self.bounce_vertical(vel)
        #             ball.set_velocity(new_vel)

        #             self._audio_service.play_sound(constants.SOUND_BOUNCE)
        #             cast["bricks"].pop(q)
        #             q -= 1
        #         q += 1
        #     if ball.get_position().get_y() >= (constants.MAX_Y - constants.BALL_HEIGHT):
        #         cast["balls"].remove(ball)
            


    def bounce_horizontal(self, point):
        """ Returns Point() with x velocity flipped """
        new = Point((point.get_x() * -1), point.get_y())
        return new

    def bounce_vertical(self, point):
        """ Returns Point() with y velocity flipped """
        new = Point(point.get_x(), (point.get_y() * -1))
        return new