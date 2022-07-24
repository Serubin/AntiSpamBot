import os

from discord.ext import commands
from dotenv import load_dotenv

import autoban.commands as autoban

def run():
    print('AntiSpam is starting')
    load_dotenv()
    token = os.getenv('discord_token')

    bot = commands.Bot(command_prefix='AntiSpam,')

    autoban.setup(bot)

    bot.run(token)

run()
