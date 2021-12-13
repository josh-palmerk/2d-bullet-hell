from game.levels.enemy_configs.enemy_config import EnemyConfig
from game.point import Point

from game.enemies.grunt import Grunt
from game.enemies.captain import Captain
from game.enemies.gatler import Gatler
from game.enemies.coward import Coward
from game.enemies.chaser import Chaser
from game.enemies.shocker import Shocker

class SandboxEnemyConfig(EnemyConfig):
    def __init__(self) -> None:
        super().__init__()

    def create_enemies(self, cast):
        """i make-a da enemies"""

        grunt1 = Grunt()
        grunt1.set_position(Point(500, 500))
        cast["enemies"].append(grunt1)


        captain1 = Captain()
        captain1.set_position(Point(1100, 600))
        cast["enemies"].append(captain1)

        gatler1 = Gatler()
        gatler1.set_position(Point(500, 700))
        cast["enemies"].append(gatler1)

        shocker1 = Shocker()
        shocker1.set_position(Point(600, 500))
        cast["enemies"].append(shocker1)

        coward1 = Coward()
        coward1.set_position(Point(100, 200))
        cast["enemies"].append(coward1)

        chaser1 = Chaser()
        chaser1.set_position(Point(1400, 800))
        cast["enemies"].append(chaser1)

