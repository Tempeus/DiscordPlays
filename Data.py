DEGRADE_LIST = [
    "Eat my ass",
    "you're about as important as a white crayon",
    "If you think Crime is gonna get you out of this, you're dumber than you look",
    "This ass is not going to eat itself",
    "You're so shit, you should uninstall",
    "Don’t talk to me. You don’t deserve to talk to me.",
    "I want you to go on your knees",
    "Let me give you some Mommy Issues"
]

FLIRTS_LIST = [
    "The only movie I want to watch is the one we both make at home",
    "You're the only mistake I want to make tonight"
]

COMPLIMENT_LIST = [
    "You're really good!",
    "You're doing great!",
    "You're awesome!",
    "You're amazing!",
    "You're a star!",
    "You're a true talent!",
    "You're on fire!",
    "You're outstanding!",
    "You're exceptional!",
    "You're a rockstar!",
    "You're the best!",
    "You're a champion!",
    "You're a genius!",
    "You're a fantastic person!",
    "You make the world a better place!",
    "You're a source of inspiration!",
    "You're a ray of sunshine!",
    "You're incredibly talented!",
    "You're a role model!",
    "You're simply the greatest!",
    "You're a superstar!",
    "You're a shining example!",
    "You're phenomenal!",
    "You're a legend!",
    "You're a top-notch individual!",
]


##################### CMD LIST #########################
VALORANT_CMD = {
    'shoot': 'Shoots gun',
    'entry': 'Holds W for 10 seconds',
    'vc': 'Uses voice chat for 10 seconds',
    'crouch' : 'Holds Crouch for 5 seconds',
    'jump' : 'make me jump',
    'drop' : 'drop my gun',
    'ult' : 'Make me use my ult',
    'pistol' : 'Switch to my pistol',
    'knife' : 'Switch to my knife',
    'reload' : 'reloads my gun',
    'random_ability' : 'Use a random ability',
    'ability1' : 'using ability 1',
    'ability2' : 'using ability 2',
    'ability3' : 'using ability 3',
}

DEBUFF_CMD = {
    'america' : 'Hold down shoot button for 10 seconds',
    'slippery_hands' : 'Drop my weapon every 10 seconds 10 timess',
    'reload_paranoia' : 'make me reload a gun every 5 seconds 20 times'
}

AI_CMD = {
    'inspire' : 'it will inspire you',
    'bot_ai' : 'Jen Jen will say an inspirational quote',
    's' : 'This is Jen Jen\'s real voice',
    'compliment_me' : 'Are you feeling down UWU? Let me cheer you up',
    'degrade_me' : 'I\'ll degrade you',
    'bully_tritin' : 'self explanatory actually',
    'joke' : 'Says a dad joke cuz this bot is a daddy <3',
    'dice' : 'rolls a regular dice',
    'd20' : 'rolls a d20 dice'
}

SOUNDPAD_CMD = {
    'bot_snore' : 'snoreeeee'
}

help_message = f"**Valorant Commands:**\n"
for command, description in VALORANT_CMD.items():
    help_message += f"{command}: {description}"
help_message += f"=======================\n"
help_message += f"**Debuffs:**\n"
for command, description in DEBUFF_CMD.items():
    help_message += f"{command}: {description}"
help_message += f"=======================\n"
help_message += f"**Sentient AI:**\n"
for command, description in AI_CMD.items():
    help_message += f"{command}: {description}"
help_message += f"=======================\n"
help_message += f"**Soundpad:**\n"
for command, description in SOUNDPAD_CMD.items():
    help_message += f"{command}: {description}"
help_message += f"=======================\n"