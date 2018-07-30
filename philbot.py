import discord
import random

adtrigger = ["flex tape", "phil", "advertise", "adhesive"]


#bot will choose a random string from this list
answer = ["It's like a handyman, in a can!", "Hi, Phil Swift here for Flex tape. The super strong water-proof tape!", "Flex tape is no ordinary tape.", "Instantly stopping the toughest leaks.", "Flex tape grips on tight and bonds instantly.", "Flex tape's powerful adhesive is so strong, it even works underwater!", "Now you can repair leaks in pools and spas without draining them!", "Flex tape is super strong!", "Once it's on, it holds on tight!", "Flex tape keeps it's grip, even in the toughtest conditions!", "Flex tape comes super wide. So you can easily patch large holes.", "I sawed this boat in half!", "Not only does Flex tape's powerful adhesive hold the boat together, but it creates a super strong water-tight seal!", "YEEEEEEEE DOGGIE!!!", "Just cut, peel, stick and seal!", "Imagine everything you can do with the power of Flex tape.", "That's a lot of damage!", "How 'bout a little more?!", "HA HA HA HA!", "NOW THAT'S A LOT OF DAMAGE!", "Let's see if it's gonna leak!", "YEP, IT LEAKS!", "WHOOO! That was a lotta fun!",
          "All right, let's seal it with Flex seal."]

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    if message.author.bot:
        return

#message is the thing we're searching for

    #if message.content.lower().startswith('heck'):
    for word in adtrigger:
        if word in message.content.lower():
            msg = (random.choice(answer)).format(message) #(random.choice(answer)) chooses a random answer
            await client.send_message(message.channel, msg)
            break

@client.event
async def on_ready():
    print('Ready to advertise.')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('')
