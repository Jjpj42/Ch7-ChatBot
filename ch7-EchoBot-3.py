# Create template
bot_template = "BOT: {0}"
# Define variables
name ="Bot"
weather = "cloudy"
badly="Bitch"
# Define a dictionary with the predefined responses
responses = {
"what's your name?": "my name is {0}".format(name),
"what's today's weather?": "the weather is {0}".format(weather),
"you fuckin bitch": "you son of a {0}".format(badly),
"default": "default message"
}
# Return the matching response if there is one, default otherwise
def respond(message):
    # Check if the message is in the responses
    if message in responses:
        # Return the matching message
        bot_message = responses[message]
    else:
    # Return the "default" message
        bot_message = responses["default"]
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