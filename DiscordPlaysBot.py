import os
from discord.ext import commands
import discord
from dotenv import load_dotenv


from gtts import gTTS
import inspirobot
import random
from dadjokes import Dadjoke
from uwuipy import uwuipy

import time
import pydirectinput
import pyautogui
import concurrent.futures

from DiscordPlays_KeyCodes import *
import Data

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

# environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
TRITIN_ID = int(os.getenv('TRITIN_ID'))
KEV_ID = int(os.getenv('KEV_ID'))
JENJEN_ID = int(os.getenv('JENJEN_ID'))
CINDY_ID = int(os.getenv('CINDY_ID'))

DISCORD_CONTROL = False

# Functions
def generate_TTS_mp3(msg):
    name = f"temp{time.time()}.mp3"
    tts = gTTS(msg)
    tts.save(name)
    return name

#We dont need this shit anymore
async def TTS(ctx, msg):
    name = generate_TTS_mp3(msg)
    time.sleep(0.5)

    if ctx.voice_client:
        source = discord.FFmpegPCMAudio(name)
        ctx.voice_client.play(source)
    else:
        await join(ctx)
        time.sleep(1)
        source = discord.FFmpegPCMAudio(name)
        ctx.voice_client.play(source)
    
    #attempt garbage collection
    time.sleep(5)
    os.remove(name)

def drop_weapon_every_interval(timer_duration):
    for i in range(10):
        # Sleep for the specified duration
        time.sleep(timer_duration)
        generate_TTS_mp3("oops")
        HoldAndReleaseKey(G, 0.7)

def reload_paranoia(timer_duration):
    for i in range(20):
        time.sleep(timer_duration)
        generate_TTS_mp3("Reloading")
        HoldAndReleaseKey(R, 0.7)

# Initialize the bot with the intents
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command(name="toggle_discord_control")
async def toggle_discord_control(ctx):
    if ctx.author.id == KEV_ID:
        global DISCORD_CONTROL
        DISCORD_CONTROL = not DISCORD_CONTROL
        await ctx.send(f"Discord Control is set to: {DISCORD_CONTROL}")


@bot.command(name='h', help="USE ME FOR BETTER HELP")
async def manual_help(ctx, command_name: str = None):
    if not command_name:
        # Provide a general help message if no specific command is specified
        await ctx.send("You can use this command to get detailed information about other commands. "
                       "Usage: `$h <command_name>`")
        await ctx.send(Data.help_message)
        return

    # Find the command based on the provided command_name
    command = bot.get_command(command_name)

    if not command:
        await ctx.send("Command not found.")
        return

    # Construct and send a detailed help message for the specified command
    help_message = f"**Command Name:** {command.name}\n"
    help_message += f"**Description:** {command.help}\n"
    help_message += f"**Usage:** {ctx.prefix}{command.name} {command.signature}\n"

    await ctx.send(help_message)

@bot.command(name='join', help='Tells the bot to join the voice channel')
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send("{} is not connected to a voice channel".format(ctx.message.author.name))
        return
    else:
        channel = ctx.message.author.voice.channel
    await channel.connect()

#################### Valorant Controls ###############################
@bot.command(name='shoot', help="Shoots gun")
async def shoot_gun(ctx):
    if DISCORD_CONTROL:
        await ctx.send("Shooting Gun", tts=True)
        def thread():
            pydirectinput.mouseDown(button="left")
            time.sleep(1)
            pydirectinput.mouseUp(button="left")
        thread_pool.submit(thread)
    else:
        await ctx.send("Discord control is not turned on")


@bot.command(name="entry", help="Holds W for 10 seconds")
async def hold_w(ctx):
    if DISCORD_CONTROL:
        await ctx.send("Holding W", tts=True)
        def thread():
            HoldAndReleaseKey(W, 10)
        thread_pool.submit(thread)
    else:
        await ctx.send("Discord control is not turned on")

@bot.command(name='vc', help="Uses voice chat for 10 seconds")
async def VC(ctx):
    if DISCORD_CONTROL:
        await ctx.send("Using voice chat for the next 10 seconds", tts=True)
        def thread():
            HoldAndReleaseKey(V, 10)
        
        thread_pool.submit(thread)
    else:
        await ctx.send("Discord control is not turned on")

@bot.command(name='crouch', help="Holds Crouch for 5 seconds")
async def crouch(ctx):
    if DISCORD_CONTROL:
        await ctx.send("Crouching for the next 5 seconds", tts=True)
        def thread():
            HoldAndReleaseKey(LEFT_CONTROL, 5)
        thread_pool.submit(thread)
    else:
        await ctx.send("Discord control is not turned on")

@bot.command(name='jump', help="Make me Jump")
async def crouch(ctx):
    if DISCORD_CONTROL:
        await ctx.send("Jump", tts=True)
        def thread():
            HoldAndReleaseKey(SPACE, 5)
        thread_pool.submit(thread)
    else:
        await ctx.send("Discord control is not turned on")

@bot.command(name='drop', help="Make me drop my gun")
async def drop(ctx):
    if DISCORD_CONTROL:
        await ctx.send("Dropping gun", tts=True)
        def thread():
            HoldAndReleaseKey(G, 0.7)
        thread_pool.submit(thread)
    else:
        await ctx.send("Discord control is not turned on")

@bot.command(name='ult', help="Make me use my ult")
async def ult(ctx):
    if DISCORD_CONTROL:
        await ctx.send("Using Ultimate", tts=True)
        def thread():
            HoldAndReleaseKey(X, 0.7)
            pydirectinput.mouseDown(button="left")
            time.sleep(1)
            pydirectinput.mouseUp(button="left")
        
        thread_pool.submit(thread)
    else:
        await ctx.send("Discord control is not turned on")

@bot.command(name='pistol', help="Switch to my pistol")
async def pistol(ctx):
    if DISCORD_CONTROL:
        await ctx.send("Switching to pistol", tts=True)
        def thread():
            HoldAndReleaseKey(TWO, 0.7)

        thread_pool.submit(thread)
    else:
        await ctx.send("Discord control is not turned on")

@bot.command(name='knife', help="Switch to my knife")
async def knife(ctx):
    if DISCORD_CONTROL:
        await ctx.send("Switching to knife", tts=True)
        def thread():
            HoldAndReleaseKey(THREE, 0.7)

        thread_pool.submit(thread)
    else:
        await ctx.send("Discord control is not turned on")

@bot.command(name='reload', help="Make me reload")
async def reload(ctx):
    if DISCORD_CONTROL:
        await ctx.send("Reloading", tts=True)
        def thread():
            HoldAndReleaseKey(R, 0.7)
        
        thread_pool.submit(thread)
    else:
        await ctx.send("Discord control is not turned on")

@bot.command(name="random_ability", help="Use a random ability")
async def random_ability(ctx):
    if DISCORD_CONTROL:
        await ctx.send("Using random ability", tts=True)
        
        def thread():
            ability_bind = [C, LEFT_ALT, E]
            random_ability = random.choice(ability_bind)
            HoldAndReleaseKey(random_ability, 0.7)
            time.sleep(0.3)
            pydirectinput.mouseDown(button="left")
            time.sleep(0.25)
            pydirectinput.mouseUp(button="left")

        thread_pool.submit(thread)
    else:
        await ctx.send("Discord control is not turned on")

@bot.command(name="ability1", help="using ability 1")
async def ability_one(ctx):
    if DISCORD_CONTROL:
        await ctx.send("Using ability", tts=True)

        def thread():
            HoldAndReleaseKey(C, 0.7)
            time.sleep(0.3)
            pydirectinput.mouseDown(button="left")
            time.sleep(0.25)
            pydirectinput.mouseUp(button="left")
        
        thread_pool.submit(thread)
    else:
        await ctx.send("Discord control is not turned on")

@bot.command(name="ability2", help="using ability 2")
async def ability_two(ctx):
    if DISCORD_CONTROL:
        await ctx.send("Using ability", tts=True)
        
        def thread():
            HoldAndReleaseKey(LEFT_ALT, 0.7)
            time.sleep(0.3)
            pydirectinput.mouseDown(button="left")
            time.sleep(0.25)
            pydirectinput.mouseUp(button="left")
        
        thread_pool.submit(thread)
    else:
        await ctx.send("Discord control is not turned on")

@bot.command(name="ability3", help="using ability 3")
async def ability_three(ctx):
    if DISCORD_CONTROL:
        await ctx.send("Using ability", tts=True)

        def thread():
            HoldAndReleaseKey(E, 0.7)
            time.sleep(0.3)
            pydirectinput.mouseDown(button="left")
            time.sleep(0.25)
            pydirectinput.mouseUp(button="left")
        
        thread_pool.submit(thread)
    else:
        await ctx.send("Discord control is not turned on")

########################################### DEBUFFS #########################################################
@bot.command(name="america", help="Hold down shoot button for 10 seconds")
async def america(ctx):
    if DISCORD_CONTROL:
        await ctx.send("What the fuck is a kilometer", tts=True)
        def tamerica():
            for i in range(20):
                time.sleep(0.5)
                pydirectinput.mouseDown(button="left")
                time.sleep(0.5)
                pydirectinput.mouseUp(button="left")

        thread_pool.submit(tamerica)
    else:
        await ctx.send("Discord control is not turned on")

@bot.command(name="slippery_hands", help="Drop my weapon every 10 seconds 10 times")
async def slippery_hands(ctx):
    if DISCORD_CONTROL:
        await ctx.send("Initiating Slippery Hands Sequence", tts=True)
        thread_pool.submit(drop_weapon_every_interval,10)
    else:
        await ctx.send("Discord control is not turned on")

@bot.command(name="reload_paranoia", help="make me reload a gun every 5 seconds 20 times")
async def reload_paranoia(ctx):
    if DISCORD_CONTROL:
        await ctx.send("Initiating reloading paranoia", tts=True)
        thread_pool.submit(reload_paranoia,5)
    else:
        await ctx.send("Discord control is not turned on")

############################### Sentient AI ###################################################
@bot.command(name='inspire', help="it will inspire you")
async def inspire(ctx):
    flow = inspirobot.flow()  # Generate a flow object
    await ctx.send(flow[0].text, tts=True)

@bot.command(name="bot_ai", help="Jen Jen will say an inspirational quote")
async def ai(ctx):
    await clear(ctx, 1)
    flow = inspirobot.flow()  # Generate a flow object
    await TTS(ctx, flow[0].text)
    await ctx.send(flow[0].text)

@bot.command(name="s", help="This is Jen Jen's real voice")
async def ai_say(ctx, *, msg):
    await clear(ctx, 0)
    await TTS(ctx, msg)

@bot.command(name="jvc", help="dont use this")
async def jvc(ctx, channel_name: str):
    await clear(ctx, 0)
    voice_channel = discord.utils.get(ctx.guild.voice_channels, name=channel_name)

    if voice_channel:
        # Connect the bot to the voice channel
        voice_client = await voice_channel.connect()

@bot.command(name="lvc", help="dont use this")
async def leave_voice(ctx):
    # Disconnect the bot from the voice channel
    await clear(ctx, 0)
    if ctx.voice_client:
        await ctx.voice_client.disconnect()

############################################# SOUNDPAD ###########################################
@bot.command(name="bot_snore", help="soundpad")
async def snore(ctx):
    if ctx.voice_client:
        source = discord.FFmpegPCMAudio("Sounds/snore.mp3")
        ctx.voice_client.play(source)
    else:
        await join(ctx)
        time.sleep(1)
        source = discord.FFmpegPCMAudio("Sounds/snore.mp3")
        ctx.voice_client.play(source)

@bot.command(name="bot_meow", help="soundpad")
async def meow(ctx):
    if ctx.voice_client:
        source = discord.FFmpegPCMAudio("Sounds/meow.mp3")
        ctx.voice_client.play(source)
    else:
        await join(ctx)
        time.sleep(1)
        source = discord.FFmpegPCMAudio("Sounds/meow.mp3")
        ctx.voice_client.play(source)


########################################## Tritin  ##########################################
@bot.command(name="compliment_me", help="let me cheer you up")
async def compliment_me(ctx):
    if ctx.author.id != TRITIN_ID:
        await ctx.send(f"{ctx.author.mention}! You look smoking hot today ;)")
    else:
        await ctx.send("Exception error occured")

@bot.command(name="degrade_me", help="Degrade me, talk me down")
async def degrade_me(ctx):
    await ctx.send("Eat my ass", tts=True)

@bot.command(name="bully_tritin", help="self explanatory actually")
async def bully_tritin(ctx):
    if ctx.author.id != TRITIN_ID:
        await ctx.send("Fuck you Tritin", tts=True)  
    else:
        await ctx.send("Why are you using this command, Tritin", tts=True)

@bot.command(name="joke", help="Says a dad joke cuz this bot is a daddy <3")
async def joke(ctx):
    dadjoke = Dadjoke()
    await ctx.send(dadjoke.joke, tts=True)

@bot.command(name="dice", help="rolls a regular dice")
async def dice(ctx):
    random_number = random.randint(1, 6)
    if ctx.author.id == TRITIN_ID:
        await ctx.send(f"{ctx.author.mention} rolled: -1 ... wait wtf how is that possible?")
    else:
        await ctx.send(f"{ctx.author.mention} rolled: {random_number}")

@bot.command(name="d20", help="rolls a d20 dice")
async def d20_dice(ctx):
    random_number = random.randint(1, 20)
    if random_number == 1 or ctx.author.id == TRITIN_ID:
        await ctx.send(f"{ctx.author.mention} rolled: 1 ... Critical Failure")
    elif random_number == 20 or ctx.author.id == KEV_ID:
        await ctx.send(f"{ctx.author.mention} rolled: 20! Critical Success!")
    else:
        await ctx.send(f"{ctx.author.mention} rolled: {random_number}")

@bot.command(name="uwu")
async def uwu(ctx,*,msg):
    uwu = uwuipy()
    await ctx.send(uwu.uwuify(msg))

######################################### DICTATOR ###############################################
@bot.command(name="clear")
async def clear(ctx, amount=5):
    # Check if the user has permission to manage messages
    # Delete the last `amount` messages in the channel
    await ctx.channel.purge(limit=amount + 1)  # +1 to include the command message


####################################### VOICE FOR SILENCED ######################################
@bot.event
async def on_message(message):
    if message.channel.name == 'silenced-people' and not message.author.bot and message.author.id == JENJEN_ID:
        ctx = await bot.get_context(message)
        await TTS(ctx, message.content)
    # Process the message as a bot command
    await bot.process_commands(message)
bot.run(TOKEN)