# bot.py
import os
from discord.ext import commands
import discord
from dotenv import load_dotenv

import keyboard
import time
import pydirectinput
import pyautogui
import concurrent.futures

from DiscordPlays_KeyCodes import *

# Define your intents
intents = discord.Intents.default()
intents.members = False  # Disable typing events, if needed
intents.presences = False  # Disable presence events, if needed
intents.message_content = True    # Enable message content updates (required for commands)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
print(TOKEN)

# Initialize the bot with the intents
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command(name='shoot', help="Shoots gun")
async def shoot_gun(ctx):
    print("executing shoot")
    pydirectinput.mouseDown(button="left")
    time.sleep(1)
    pydirectinput.mouseUp(button="left")
    await ctx.send("shooting gun")

@bot.command(name='vc', help="Uses voice chat for 10 seconds")
async def VC(ctx):
    HoldAndReleaseKey(V, 10)
    await ctx.send("Holding V for 10 seconds")

@bot.command(name='crouch', help="Holds Crouch for 5 seconds")
async def crouch(ctx):
    HoldAndReleaseKey(LEFT_CONTROL, 5)
    await ctx.send("Holding Crouch for 5 seconds")

@bot.command(name='jump', help="Make me Jump")
async def crouch(ctx):
    HoldAndReleaseKey(SPACE, 5)
    await ctx.send("JUMP")

@bot.command(name='drop', help="Make me drop my gun")
async def crouch(ctx):
    HoldAndReleaseKey(G, 0.7)
    await ctx.send("Dropping gun")

bot.run(TOKEN)