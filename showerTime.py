from ohbotMac import ohbot as ob
from moveLib import randomMotionSmall, randomMotionBig, endAndRest, listOfMoves, listOfMotors, chooseBigOrSmall
import random

ob.reset()
ob.wait(2)

ob.setVoice("Samantha")

listOfMoves = [i for i in range(random.randint(50, 100))]
print(len(listOfMoves))

for move in listOfMoves:
    chooseBigOrSmall()

ob.reset()
ob.wait(1)

endAndRest()
ob.wait(1)

ob.close()