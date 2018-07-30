import discord

swear = ["heck", "dagnabbit", "nabbit", "jerk", "dumby", "butt", "slut", "turd", "frick", "freak", "jeez", "darn", "dang", "golly", "gee", "piss", "damn", "ass", "gosh", "dong", "crap", "shit", "fuck", "bitch", "bastard"]

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
    for word in swear:
        if word in message.content.lower():
            msg = 'Did you just swear on my Christian server, {0.author.mention}?!'.format(message)
            await client.send_message(message.channel, msg)
            break

@client.event
async def on_ready():
    print('Ready to ban some sinners.')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('')
