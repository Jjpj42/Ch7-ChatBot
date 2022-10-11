import random
import re

# Create templates
bot_template = "BOT : {0}"
user_template = "USER : {0}"
rules = {   'do you think (.*)':    [
                                    'No chance'
                                    ],
            'do you remember (.*)': [
                                    'Did you think I would forget {0}',
                                   
                                    ],
            'I want (.*)':          [
                                    
                                    'Why do you want {0}'
                                    ],
                                    
            'if (.*)':              [
                                    "Do you really think it's likely that {0}",
                                    'Do you wish that {0}',
                                    'What do you think about {0}',
                                    'Really--if {0}'
                                    ]
        }
# Define respond()

def match_rule(rules, message):
    response, phrase = "default", None
    # Iterate over the rules dictionary
    for pattern, responses in rules.items():
        # Create a match object
        match = re.search(pattern,message)
        if match is not None:
            # Choose a random response
            response = random.choice(responses)
            if '{0}' in response:
                phrase = match.group(1)

    # Return the response and phrase
    return response.format(phrase)

def respond(message):
    # Call match_rule
    test = match_rule(message)
    ____ = ____

    if '{0}' in response:
        # Replace the pronouns in the phrase
        phrase = ____
        # Include the phrase in the response
        response = ____
    return response

def replace_pronouns(message):
            message = message.lower()
            if 'me' in message:
            # Replace 'me' with 'you'
                 re.sub('me','you', message )
            if 'my' in message:
            # Replace 'my' with 'your'
                 re.sub('my','your', message )
            if 'your' in message:
            # Replace 'your' with 'my'
                 re.sub('your','my', message )
            if 'you' in message:
            # Replace 'you' with 'me'
                re.sub('you','I', message )
            if 'i' in message:
            # Replace 'you' with 'me'
                re.sub('i','you', message )
            return message

def send_message(message):
    # Print user_template including the user_message
    print(user_template.format(message))
    # Get the bot's response to the message
    response = match_rule(rules,message)
    # Print the bot template including the bot's response.
    print(bot_template.format(response))
# Send the messages
send_message("do you remember your last birthday")
send_message("do you think humans should be worried about AI")
send_message("I want a robot friend")
# send_message("what if you could be anything you wanted")