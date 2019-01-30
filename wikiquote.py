import wikiquotes
from ohbotMac import ohbot
import random

ohbot.reset()
ohbot.wait(1)

print("Sending the request")

theList = wikiquotes.get_quotes("Musk", "English")

if theList:

    ohbot.reset()
    ohbot.wait(1)

    print("Success")
    print(theList)
    print(len(theList))
    text = theList[random.randint(0, len(theList)-1)]
    print(text)

    ohbot.say(text)
    ohbot.wait(1)

else:
    print("Problem connecting to the server")

print("Sending the second request")
quoteOfTheDay = wikiquotes.quote_of_the_day("English")
newText = quoteOfTheDay[0]
print(newText)
print(type(newText))
#
# ohbot.say(str(newText))

ohbot.close()


