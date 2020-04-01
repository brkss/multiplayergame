from files.pygame_functions import *
from files.player import Player
from files.api import api
import time

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


# player
player = Player(300, 200, 0, "img/smalllinks.gif", name, 32, 8)
player.draw()

# connect to api
"""
api = api('http://localhost:3000', name)
api.sendData(17, 300, 200)
enemyData = api.getData()

# Enemy
enemy = Player(int(enemyData[1]), int(enemyData[2]), 0, "img/smalllinks.gif", "Enemy", 32, 8)
enemy.draw()
"""

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

while True:
    if clock() > nextFrame:  # We only animate our character every 80ms.
        frame = (frame + 1) % 8  # There are 8 frames of animation in each direction
        nextFrame += 80  # so the modulus 8 allows it to loop
        food_frame = (food_frame + 1) % 26

    if keyPressed("right"):
        currentFrame = 0 * 8 + frame
        player.move(currentFrame, 20, 0)
        lastKey = "right"

    elif keyPressed("down"):
        currentFrame = 1 * 8 + frame
        player.move(currentFrame, 0, 20)
        lastKey = "down"

    elif keyPressed("left"):
        currentFrame = 2 * 8 + frame
        player.move(currentFrame, -20, 0)
        lastKey = "left"

    elif keyPressed("up"):
        currentFrame = 3 * 8 + frame
        player.move(currentFrame, 0, -20)
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

    #enemyData = api.getData()

    #print(enemyData)
    #enemy.getData(int(enemyData[0]), int(enemyData[1]), int(enemyData[2]))
    #api.sendData(currentFrame, player.x, player.y)
    changeSpriteImage(foodSprite, 0 * 26 + food_frame)
    tick(120)

endWait()
