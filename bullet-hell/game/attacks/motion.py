
class Motion():
    """ uh idk what im doing here """
    def __init__(self):
        self._timer = 0

    def update(self):
        """ update all the things that need to happen on this frame """

        raise NotImplementedError("update() not implemented in superclass")

    def decrement_timer(self):
        """ just a -=1 to self._timer """
        self._timer -= 1

    def set_timer(self, value):
        self._timer = value

    def get_timer(self):
        return self._timer
