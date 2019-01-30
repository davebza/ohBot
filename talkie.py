from ohbotMac import ohbot
import random

def randomMotion():
    "This function makes a random movement for Ohbot to perform, and then chooses a random wait time after the movement"
    ohbot.move(random.randint(0, 6), random.randint(0, 9), random.randint(1, 10))
    ohbot.wait(getRandomDecimal())

def getRandomDecimal():
    """This function creates a random decimal between 0.1 and 0.9 for the wait times between moves"""
    decimal = float(random.randrange(1, 9)/10)
    return decimal

ohbot.reset()
ohbot.wait(1)

ohbot.setVoice("Samantha")

ohbot.say("Hi sean and mummy and daddy")
ohbot.say("i love you")
ohbot.say("do you love me yes or no ")

love = input("write your answer")

if love == "yes":
    ohbot.say("yes yes yes i want to marry you")

elif love == "no":
    ohbot.say("moo moo moo moo    no no nope")
else:
    ohbot.say("I don't understand")

listOfMoves = [i for i in range(random.randint(1, 20))]

for move in listOfMoves:
    randomMotion()

ohbot.reset()
ohbot.wait(2)

#close to exit
ohbot.close()