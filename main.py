from files.pygame_functions import *
from files.player import Player
from files.bullet import Bulet
from files.api import api
import time
import math

screenSize(600, 600)
setBackgroundImage("img/turf.png")

wordBox = makeTextBox(10, 80, 300, 0, "Enter yout name here", 15, 24)
showTextBox(wordBox)
name = textBoxInput(wordBox)
hideTextBox(wordBox)
# set up


lastKey = "down"
currentFrame = 0

data = []


def getData():
    # time.sleep(0.1)
    del data[:]
    f = open("data.txt", "r")
    for x in f:
        data.append(int(x.replace("\n", "")))
    # print(data)


def saveData(index, x, y):
    # time.sleep(0.06)
    fl = open("data2.txt", "w")
    fl.write(str(index) + "\n")
    fl.write(str(x) + "\n")
    fl.write(str(y) + "\n")


def touch(xa, xb, ya, yb):
    d = math.sqrt((math.pow(xa - xb, 2)) + (math.pow(ya - yb, 2)))
    if d <= 27:
        return True
    return False

def getDir(index):
    if index < 8:
        return "right"
    elif index >= 8 and index < 16:
        return "down"
    elif index >= 16 and index < 24:
        return "left"
    return "up"



# player
player = Player(300, 200, 0, "img/smalllinks.gif", name, 32, 8, sta=True)
player.draw()
# bullet


# connect to api
api = api('http://localhost:3000', name)
api.sendData(17, 300, 200)
enemyData = api.getData()
print(enemyData)
# Enemy
enemy = Player(int(enemyData[1]), int(enemyData[1]), 0, "img/smalllinks.gif", "Enemy", 32, 8)
enemy.draw()

# food
foodSprite = makeSprite('img/waterlinks.gif', 26)
moveSprite(foodSprite, 50, 50, True)
showSprite(foodSprite)

# box
boxSprite = makeSprite('img/box.png')
moveSprite(boxSprite, 300, 300)
showSprite(boxSprite)

nextFrame = clock()
frame = 0
food_frame = 0
bullet = Bulet()

enemyBulet = Bulet()

while True:
    if clock() > nextFrame:  # We only animate our character every 80ms.
        frame = (frame + 1) % 8  # There are 8 frames of animation in each direction
        nextFrame += 80  # so the modulus 8 allows it to loop
        food_frame = (food_frame + 1) % 26

    if keyPressed('space'):
        bullet.shoot(lastKey, player.x, player.y)
        api.sendData(currentFrame, player.x, player.y, True, player.x, player.y)
    elif bullet.bulletOff:
        bullet.shoot(lastKey, player.x, player.y)
        if touch(bullet.bx, enemy.x, bullet.by, enemy.y):
            enemy.hp -= 1
            print(enemy.hp)
            enemy.hit()
            bullet.shoot(lastKey, player.x, player.y, True)

    if keyPressed("right"):
        currentFrame = 0 * 8 + frame
        player.move(currentFrame, 25, 0)
        lastKey = "right"

    elif keyPressed("down"):
        currentFrame = 1 * 8 + frame
        player.move(currentFrame, 0, 25)
        lastKey = "down"

    elif keyPressed("left"):
        currentFrame = 2 * 8 + frame
        player.move(currentFrame, -25, 0)
        lastKey = "left"

    elif keyPressed("up"):
        currentFrame = 3 * 8 + frame
        player.move(currentFrame, 0, -25)
        lastKey = "up"


    else:
        if lastKey == "down":
            currentFrame = 1 * 8 + 5
            player.move(currentFrame, 0, 0)
        elif lastKey == "up":
            currentFrame = 3 * 8 + 7
            player.move(currentFrame, 0, 0)
        elif lastKey == "right":
            currentFrame = 0 * 8 + 7
            player.move(currentFrame, 0, 0)
        elif lastKey == "left":
            currentFrame = 2 * 8 + 1
            player.move(currentFrame, 0, 0)

    enemyData = api.getData()
    enemyDir = getDir(int(enemyData[0]))
    if enemyData[3]:
        enemyBulet.shoot(enemyDir, int(enemyData[1]), int(enemyData[2]))
    elif enemyBulet.bulletOff:
        enemyBulet.shoot(enemyDir, int(enemyData[1]), int(enemyData[2]))
        if touch(enemyBulet.bx, player.x, enemyBulet.by, player.y):
            player.hp -= 1
            print(enemy.hp)
            enemy.hit()
            enemyBulet.shoot(lastKey, player.x, player.y, True)

    print(enemyData)
    enemy.getData(int(enemyData[0]), int(enemyData[1]), int(enemyData[2]))
    api.sendData(currentFrame, player.x, player.y)

    changeSpriteImage(foodSprite, 0 * 26 + food_frame)
    tick(120)

endWait()
