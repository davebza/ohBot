from ohbotMac import ohbot

ohbot.reset()
ohbot.wait(2)

ohbot.setVoice("Fiona")
ohbot.say("Hello Maggie and Frederik")

ohbot.wait(1)

ohbot.move(4, 7, 10)
ohbot.move(5, 7, 10)

ohbot.reset()
ohbot.wait(1)

ohbot.close()