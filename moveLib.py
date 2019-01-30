from ohbotMac import ohbot
import random

def randomMotionBig():
    "This function makes a large, dramatic random movement for Ohbot to perform, and then chooses a random wait time after the movement"
    ohbot.move(random.randint(0, 6), random.randint(0, 10), random.randint(1, 10))
    ohbot.wait(getRandomDecimal())

def randomMotionSmall():
    "This function makes a small, random movement for Ohbot to perform, and then chooses a random wait time after the movement"
    ohbot.move(random.randint(0, 6), random.randint(3, 6), random.randint(1, 10))
    ohbot.wait(getRandomDecimal())

def chooseBigOrSmall():

    theChoice = random.randint(1, 100)
    if theChoice < 33:
        theMove = randomMotionBig()
        # print("big")
    else:
        theMove = randomMotionSmall()
        # print("small")

    return theMove

def nodHead():
    "This function nods head and says yes three times"
    ohbot.say("Yes Yes Yes", False)
    ohbot.move(ohbot.HEADNOD, 0, 3)
    ohbot.wait(.2)
    ohbot.move(ohbot.HEADNOD, 10, 10)
    ohbot.wait(.3)
    ohbot.move(ohbot.HEADNOD, 5, 5)
    ohbot.wait(1)

def shakeHead():
    "This function shakes head and says no three times"
    ohbot.say("NO No No", False)
    ohbot.move(NECK, 0, 3)
    ohbot.wait(.2)
    ohbot.move(NECK, 10, 10)
    ohbot.wait(.3)
    ohbot.move(NECK, 5, 5)
    ohbot.wait(1)

def blink():
    ohbot.move(EYELIDS, 0, 10)
    ohbot.wait(.2)
    ohbot.move(EYELIDS, 7, 10)
    ohbot.wait(.4)

def focus():
    ohbot.move(ohbot.HEADNOD, 0, 3)
    ohbot.wait(.2)
    ohbot.move(EYELIDS, 0, 10)
    ohbot.wait(.8)
    ohbot.move(ohbot.HEADNOD, 7, 10)
    ohbot.wait(.3)
    ohbot.move(EYELIDS, 7, 10)
    ohbot.wait(1)
    ohbot.move(ohbot.HEADNOD, 5, 3)
    ohbot.wait(.3)

def getRandomDecimal():
    """This function creates a random decimal between 0.1 and 0.9 for the wait times between moves"""
    decimal = float(random.randrange(1, 9)/10)
    return decimal

def endAndRest():
    ohbot.reset()
    ohbot.wait(1)
    ohbot.move(3, 0, 2)

ohbot.reset()
ohbot.wait(1)

ohbot.setVoice("Samantha")

#constants for motors
NOD = 0
NECK = 1
EYEBALLS = 2
EYELIDS = 3
TOPLIP = 4
BOTTOMLIP = 5
EYESOCKETS = 6

listOfMotors = [NOD, NECK, EYEBALLS, EYELIDS, TOPLIP, BOTTOMLIP, EYESOCKETS]


# blink()
# focus()
# nodHead()
# shakeHead()


listOfMoves = [i for i in range(random.randint(50, 100))]
# print(len(listOfMoves))
#
# for move in listOfMoves:
#     chooseBigOrSmall()

# ohbot.setVoice("Alex")
# ohbot.say("Mish, You will be next.")


endAndRest()
ohbot.wait(2)

#close to exit
ohbot.close()