import re
# Define replace_pronouns()
def replace_pronouns(message):
    message = message.lower()
    '''if 'me' in message:
        # Replace 'me' with 'you'
        return re.sub('me','you', message )
    if 'my' in message:
        # Replace 'my' with 'your'

        return re.sub('my','your', message )
    if 'your' in message:
        # Replace 'your' with 'my'
        return re.sub('your','my', message )
    if 'you' in message:
        # Replace 'you' with 'me'
        return re.sub('you','I', message )
    if 'i' in message:
        # Replace 'you' with 'me'
        return re.sub('i','you', message )'''



    '''message = re.sub('me','you',message)
        message = re.sub('i','you', message )
        message = re.sub('your','my', message )
        message = re.sub('you','I', message )
        message = re.sub('my','your', message )'''

    if 'me' in message:
            # Replace 'me' with 'you'
            message = re.sub('me','you', message )

    if 'my' in message:
            # Replace 'my' with 'your'
             message = re.sub('my','your', message )

    if 'i' in message:
            # Replace 'you' with 'me'
            message = re.sub('i','you', message )

        
        
    return message
print(replace_pronouns("my last birthday"))
print(replace_pronouns("go with me to Florida"))
print(replace_pronouns("I had my own castle"))