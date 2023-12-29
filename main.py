import discord

from discord.ext import commands
from config import BOT_TOKEN, COMMAND_PREFIX

# Configuration du bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=COMMAND_PREFIX, intents=intents)

# Événement lorsque le bot est prêt
@bot.event
async def on_ready():
    print(f"{bot.user.name} is connected to Discord !")

# Lance le bot avec le token récupéré depuis le fichier
bot.run(BOT_TOKEN)


######################################### COMMANDS ##############################
