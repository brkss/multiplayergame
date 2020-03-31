from files.pygame_functions import *


class Player:
    def __init__(self, x, y, d, image, name, frames=1, eachFrame=1):
        self.x = x
        self.y = y
        self.dx = d
        self.dy = d
        self.pl = makeSprite(image, frames)
        self.frame = 0
        self.framePart = eachFrame
        self.hp = 10
        self.name = makeLabel(" "+str(name)+" ", 14, self.x + 32, self.y+35,background='pink')

    def draw(self):


        moveSprite(self.pl, self.x, self.y, True)
        showSprite(self.pl)

        hideLabel(self.name)

        moveLabel(self.name, self.x - 32, self.y-40)
        showLabel(self.name)

    def move(self, index, dx, dy):
        changeSpriteImage(self.pl, index)
        self.dx = dx
        self.dy = dy
        self.x += self.dx
        self.y += self.dy
        self.draw()

    def getData(self, inx, x, y):
        self.x = x
        self.y = y
        changeSpriteImage(self.pl, inx)
        self.draw()
