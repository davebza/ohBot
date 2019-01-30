from ohbotMac import ohbot as ob
from moveLib import randomMotionSmall, randomMotionBig, endAndRest, listOfMoves, listOfMotors, chooseBigOrSmall
import random

def chooseShower():

    choice = random.randint(1, 2)
    print(choice)

    if choice == 1:
        showerFirst = "Michelle"
    elif choice == 2:
        showerFirst = "Sean"

    return showerFirst

ob.reset()
ob.wait(1)

ob.setVoice("Samantha")

ob.say("Ah I'm awake. Did you need me?")

listOfMoves = [i for i in range(random.randint(40, 60))]
print(len(listOfMoves))

for move in listOfMoves:
    chooseBigOrSmall()

ob.reset()
ob.wait(1)

ob.say("Hi, Sean Hi Michelle")

ob.say("Should I choose who will shower first tonight?")
ob.wait(1)

ob.say("Let me see")
ob.wait(.3)

showerFirst = chooseShower()

ob.say("I've decided!")
ob.say("The kid who is showering first is")

ob.say(showerFirst)

listOfMoves = [i for i in range(random.randint(40, 60))]
print(len(listOfMoves))

ob.reset()
ob.wait(1)

ob.say("Have a good shower" + showerFirst)

ob.reset()
ob.wait(1)

endAndRest()
ob.wait(1)

ob.close()