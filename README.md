# 2d-bullet-hell

This is the Beta Release of the Bullet Hell game I am creating for the final project of CSE210. There are unfortunately no objectives in this version., though you can see your health value and enemies are both bloodthirsty and destructible (except the dummy).

At the moment there are a few big improvements and innovations since the Alpha release. 
-Unit vectors. Every actor now moves at a consistent speed regardless of which direction it's going, diagonal or cardinal. This unit vector (x,y values that make a radius of 1) is multiplied by the actor's default speed for a pretty consistent pysics experience.

-I have devised a bit of trigonometry to allow angle adjustments on shots, making for some more interesting shot patterns such as shotgun sprays, circles, semi-circles, etc.

-More importantly than that, I have created a Motion object with an update() method that is called every frame until its timer expires. This allows for interesting game mechanics such as a dodge roll (implemented and functional), a burst-rifle shot (not yet implemented), a shielding action (not yet implemented), you name it and now it's possible and relatively easy to implement.

I expect to add many of these types of features by the time of the Stable Release.