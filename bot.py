# invite link:
# https://discord.com/oauth2/authorize?client_id=818268022354608158&permissions=8&scope=bot

import discord
from discord.ext import commands
from discord.utils import get

import json
# import ChessClient # for all of the Chess.com API data scrapping
import os

intents = discord.Intents.all()
client = commands.Bot(command_prefix = '.', intents=intents)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="Looking for Yugioh Cards"))
    print("Launch Successful!")
    print('We have logged in as {0.user}'.format(client))
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))

@client.event
async def on_message(message):
    await client.process_commands(message)

def getToken():
    # code to open and read token
    return os.environ.get('TOKEN')
client.run("ODE4MjY4MDIyMzU0NjA4MTU4.YEVlew.BFwImybWDJzMV4Xz-YUrn4Xsgig")