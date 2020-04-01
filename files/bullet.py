from files.pygame_functions import *


class Bulet:
    def __init__(self):
        self.bx = 0
        self.by = 0
        self.buletIndex = 0
        self.bulletOff = False
        self.bulet = makeSprite('img/buletlinks.gif', 4)

    def BordCo(self, x, y):
        if x >= 576 or x <= 24 or y >= 576 or y <= 24:
            return True
        return False

    def shoot(self, dirc, x, y , touch=False):
        index = 0
        if not self.bulletOff:
            self.bx = x
            self.by = y
            if dirc == "up":
                self.buletIndex = 1
            elif dirc == "down":
                self.buletIndex = 2
            elif dirc == "left":
                self.buletIndex = 3
            elif dirc == "right":
                self.buletIndex = 0

        if self.buletIndex == 1:
            self.by += -5
        elif self.buletIndex == 2:
            self.by += 5
        elif self.buletIndex == 3:
            self.bx += -5
        elif self.buletIndex == 0:
            self.bx += 5

        if self.BordCo(self.bx, self.by) or touch :

            self.bulletOff = False
            hideSprite(self.bulet)

        else:
            changeSpriteImage(self.bulet, self.buletIndex)
            moveSprite(self.bulet, self.bx, self.by, True)
            showSprite(self.bulet)
            self.bulletOff = True
