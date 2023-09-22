# bot.py
import os
from discord.ext import commands
import discord
from dotenv import load_dotenv
from gtts import gTTS
import playsound
import os
import inspirobot


import keyboard
import time
import pydirectinput
import pyautogui
import concurrent.futures

from DiscordPlays_KeyCodes import *

# Message Queue Variables #
MAX_QUEUE_LENGTH = 20
MAX_WORKERS = 100 # Maximum number of threads you can process at a time 

last_time = time.time()
message_queue = []
thread_pool = concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS)
active_tasks = []
pyautogui.FAILSAFE = False

# Define your intents
intents = discord.Intents.default()
intents.members = False  # Disable typing events, if needed
intents.presences = False  # Disable presence events, if needed
intents.message_content = True    # Enable message content updates (required for commands)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
print(TOKEN)

# Functions
def text_to_speech(msg):
        name = f"temp{time.time()}.mp3"
        tts = gTTS(msg)
        tts.save(name)
        time.sleep(1) 
        playsound.playsound(name)
        os.remove(name)

def drop_weapon_every_interval(timer_duration):
    for i in range(10):
        # Sleep for the specified duration
        time.sleep(timer_duration)
        text_to_speech("oops")
        HoldAndReleaseKey(G, 0.7)

def reload_paranoia(timer_duration):
    for i in range(20):
        time.sleep(timer_duration)
        text_to_speech("Reloading")
        HoldAndReleaseKey(R, 0.7)

# Initialize the bot with the intents
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command(name='join', help='Tells the bot to join the voice channel')
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send("{} is not connected to a voice channel".format(ctx.message.author.name))
        return
    else:
        channel = ctx.message.author.voice.channel
    await channel.connect()

# @bot.command(name='play_song', help='To play song')
# async def play(ctx,url):
#     try :
#         server = ctx.message.guild
#         voice_channel = server.voice_client

#         async with ctx.typing():
#             voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source=filename))
#         await ctx.send('**Now playing:** {}'.format(filename))
#     except:
#         await ctx.send("The bot is not connected to a voice channel.")

@bot.command(name='shoot', help="Shoots gun")
async def shoot_gun(ctx):
    await ctx.send("shooting gun")
    print("executing shoot")
    pydirectinput.mouseDown(button="left")
    time.sleep(1)
    pydirectinput.mouseUp(button="left")

@bot.command(name='vc', help="Uses voice chat for 10 seconds")
async def VC(ctx):
    await ctx.send("Holding V for 10 seconds")
    HoldAndReleaseKey(V, 10)

@bot.command(name='crouch', help="Holds Crouch for 5 seconds")
async def crouch(ctx):
    await ctx.send("Holding Crouch for 5 seconds")
    HoldAndReleaseKey(LEFT_CONTROL, 5)
 
@bot.command(name='jump', help="Make me Jump")
async def crouch(ctx):
    await ctx.send("JUMP")
    HoldAndReleaseKey(SPACE, 5)

@bot.command(name='drop', help="Make me drop my gun")
async def drop(ctx):
    await ctx.send("Dropping gun")
    HoldAndReleaseKey(G, 0.7)

@bot.command(name='ult', help="Make me use my ult")
async def ult(ctx):
    await ctx.send("Using Ult")
    HoldAndReleaseKey(X, 0.7)
    pydirectinput.mouseDown(button="left")
    time.sleep(1)
    pydirectinput.mouseUp(button="left")

@bot.command(name='pistol', help="Switch to my pistol")
async def pistol(ctx):
    HoldAndReleaseKey(TWO, 0.7)

@bot.command(name='knife', help="Switch to my knife")
async def pistol(ctx):
    HoldAndReleaseKey(THREE, 0.7)

@bot.command(name='reload', help="Make me reload")
async def pistol(ctx):
    HoldAndReleaseKey(R, 0.7)

@bot.command(name="random_ability", help="Use a random ability")
async def random_ability(ctx):
      print()

@bot.command(name="ability1", help="using ability 1")
async def ability_one(ctx):
    text_to_speech("Initiating Ability Usage Sequence")
    HoldAndReleaseKey(C, 0.7)
    time.sleep(0.3)
    pydirectinput.mouseDown(button="left")
    time.sleep(0.25)
    pydirectinput.mouseUp(button="left")
      
@bot.command(name="ability2", help="using ability 2")
async def ability_two(ctx):
    text_to_speech("Initiating Ability Usage Sequence")
    HoldAndReleaseKey(LEFT_ALT, 0.7)
    time.sleep(0.3)
    pydirectinput.mouseDown(button="left")
    time.sleep(0.25)
    pydirectinput.mouseUp(button="left")

@bot.command(name="ability3", help="using ability 3")
async def ability_three(ctx):
    text_to_speech("Initiating Ability Usage Sequence")
    HoldAndReleaseKey(E, 0.7)
    time.sleep(0.3)
    pydirectinput.mouseDown(button="left")
    time.sleep(0.25)
    pydirectinput.mouseUp(button="left")

@bot.command(name="slippery_hands", help="Drop my weapon every 10 seconds 10 times")
async def slippery_hands(ctx):
    text_to_speech("Initiating Slippery Hands Sequence")
    drop_weapon_every_interval(10)

@bot.command(name="reload_paranoia", help="make me reload a gun every 5 seconds 20 times")
async def reload_paranoia(ctx):
    text_to_speech("Initiating reloading paranoia")
    reload_paranoia(5)

@bot.command(name='inspire', help="it will inspire you")
async def inspire(ctx):
    flow = inspirobot.flow()  # Generate a flow object
    await ctx.send(flow[0].text)

bot.run(TOKEN)