# Import the random module
import random
# Create template
bot_template = "BOT: {0}"

name = "Bot"
weather = "cloudy"
food="Patkapow" , "Tomyum"
# Define a dictionary containing a list of responses for each message
responses = {
    "what's your name?": ["my name is {0}".format(name),
                            "they call me {0}".format(name),
                            "I am {0}".format(name)
    ],
    "what's today's weather?": [
                            "the weather is {0}".format(weather),
                            "it's {0} today".format(weather)
    ],
    "what should I eat": ["Eat This :  {0}".format(food),
                        "Must Eat This : {0}".format(food)],
    "default": ["default message"]
}

def respond(message):
    # Check if the message is in the responses
    if message in responses:
       # Return a random matching response
        bot_message = random.choice(responses[message])
    else:
   # Return a random "Default" response
        bot_message = random.choice(responses["default"])
    return bot_message


#print a message to the bot
def send_message(message):
    response = respond(message)
    print(bot_template.format(response))


print(bot_template.format("Hi"))
while (True):
    value = input("USER : ")
    if(value != '0'):
        send_message(value)
    else:
        break