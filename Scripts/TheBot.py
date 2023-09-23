import discord
from discord.ext import commands
import thanks_command 
import listening
import test_bench

from dotenv import dotenv_values
import var

secrets = dotenv_values("shhh.env")
intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    
    permissions = discord.Permissions(2064000588865)  # Create Permissions object from the permission integer

listening.setup(bot)

test_bench.setup(bot)

thanks_command.setup(bot)

bot.run(secrets['bot_token'])
