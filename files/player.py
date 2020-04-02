from files.pygame_functions import *


class Player:
    def __init__(self, x, y, d, image, name, frames=1, eachFrame=1,sta=False):
        self.x = x
        self.y = y
        self.dx = d
        self.dy = d
        self.pl = makeSprite(image, frames)
        self.frame = 0
        self.framePart = eachFrame
        self.hp = 10
        self.playerName = name
        self.name = makeLabel(" " + str(self.playerName) + " "+str(self.hp), 14, self.x + 32, self.y + 35, background='pink')
        self.bulet = makeSprite('img/buletlinks.gif', 4)
        self.bx = self.x
        self.by = self.y
        self.bulletOff = False
        self.buletIndex= 0
        self.isShooted = False
        if sta :
            self.xt = 550
            self.lb = "Me"
        else :
            self.xt = 50
            self.lb = "Enemy"
        self.yt = 50
        self.score = makeLabel(self.lb+" : "+str(self.hp), 16, self.xt, self.yt, background='white')
        showLabel(self.score)

    def draw(self):
        moveSprite(self.pl, self.x, self.y, True)
        showSprite(self.pl)
        hideLabel(self.name)
        moveLabel(self.name, self.x - 32, self.y - 40)
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

    def BordCo(self, x, y):
        if x >= 576 or x <= 24 or y >= 576 or y <= 24:
            return True
        return False

    def hit(self):
        self.name = makeLabel(" " + str(self.playerName) + " " + str(self.hp)[0], 14, self.x + 32, self.y + 35, background='pink')
        hideLabel(self.name)
        moveLabel(self.name, self.x - 32, self.y - 40)
        showLabel(self.name)
        self.score = makeLabel(self.lb+" : "+str(self.hp)[0], 16, self.xt, self.yt, background='white')
        moveLabel(self.score, self.xt, self.yt)
        showLabel(self.score)

"""
    def shoot(self, dirc, x, y):
        index = 0
        if not self.bulletOff:
            self.bx = x
            self.by = y
            self.hp -=1
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

        if self.BordCo(self.bx, self.by):
            self.bulletOff = False
            hideSprite(self.bulet)
            self.bx = self.x
            self.by = self.y
        else:
            changeSpriteImage(self.bulet, self.buletIndex)
            moveSprite(self.bulet, self.bx, self.by, True)
            showSprite(self.bulet)
            self.bulletOff = True

"""




