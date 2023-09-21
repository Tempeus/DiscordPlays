# bot.py
import os
from discord.ext import commands
import discord
from dotenv import load_dotenv

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

@bot.command(name='hello', help="Say hiiiiii")
async def hello(ctx):
    print("executing hello")
    await ctx.send("Hello, I am your bot!")

@bot.command(name='shoot', help="Shoots gun")
async def shoot_gun(ctx):
    print("executing shoot")
    await ctx.send("shooting gun")

bot.run(TOKEN)