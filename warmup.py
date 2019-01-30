from ohbotMac import ohbot

ohbot.setVoice("Fiona")

def warmUp(motor, movePosition, speed):
    ohbot.move(motor, movePosition, speed)
    ohbot.wait(WAITTIME)

def giveInfo(motor):
    motorList = ["neck", "eye balls", "eye lids", "top lip", "bottom lip", "eye sockets"]
    currentMotor = motorList[motor - 1]
    ohbot.say("checking" + currentMotor)

def yes():
    ohbot.move(ohbot.HEADNOD, 0, 10)
    ohbot.wait(.1)
    ohbot.move(ohbot.HEADNOD, 10, 10)
    ohbot.wait(.5)
    ohbot.move(ohbot.HEADNOD, 5, 10)
    ohbot.wait(.1)


#define constants for motors:

NECK = 1
EYEBALLS = 2
EYELIDS = 3
TOPLIP = 4
BOTTOMLIP = 5
EYESOCKETS = 6

MOVESPEED = 10
WAITTIME = 1

#make a list of motors:
motors = [NECK, EYEBALLS, EYELIDS, TOPLIP, BOTTOMLIP, EYESOCKETS]

# Reset Ohbot
ohbot.reset()
ohbot.wait(WAITTIME)

ohbot.say("Warm up time. I'm going to check all my motors one by one.")

# for motor in motors:
#     giveInfo(motor)
#     warmUp(motor, 1, MOVESPEED)
#

ohbot.say("Warm up complete. I'm good to go.")
yes()

# Reset Ohbot
ohbot.reset()
ohbot.wait(WAITTIME)
#close to exit
ohbot.close()