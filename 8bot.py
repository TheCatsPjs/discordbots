import random
import requests
import asyncio

from discord import Game
from discord.ext.commands import Bot

BOT_PREFIX = ("!", "/")
TOKEN = ""

client = Bot(command_prefix=BOT_PREFIX)

@client.command(name='8ball',
                     description="Answers a Yes/No question.",
                     brief="Answering questions from beyond.",
                     aliases=['eight_ball', 'eightball', 'eightboy', 'atebowl', '8boy', 'eighty', 'bally', '8_ball', '8bot', 'eightbot', 'eight_bot', '8'],
                     pass_context=True)
async def eight_ball(context):
    possible_responses = [
        "Yes, of course",
        "Heck no",
        "Absolutely",
        "What do you think",
        "Ha... maybe",
        "Duh",
        "That's a stupid question, you are stupid",
        "Yup",
        "Naw",
        "Ya boi",
        "No, of course not",
        "It is certain",
        "It is decidedly so",
        "Without a doubt",
        "Definitely",
        "As I see it, yes",
        "You may rely on it",
        "Most likely",
        "Outlook... bad",
        "Yesh",
        "Signs point to yes",
        "Don't count on it",
        "My reply is no",
        "My sources say yes",
        "Very doubtful",
        "It is likely"
    ]

    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)

@client.command()
async def square(number):
    squared_value = int(number) * int(number)
    await client.say(str(number) + " squared is " + str(squared_value))


@client.event
async def on_ready():
    await client.change_presence(game=Game(name="Minecraft"))
    print("Logged in as " + client.user.name)

@client.command()
async def bitcoin():
    url = 'https://api.coindesk.com/v1/bpi/currentprice/<CODE>.json'
    response = requests.get(url)
    value = response.json()['bpi']['USD']['rate']
    await client.say("Bitcoin price is: $" + value)

async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(3600)


client.loop.create_task(list_servers())

client.run(TOKEN)
