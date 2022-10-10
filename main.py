import discord
import yaml
from discord.ext import commands
import os
import logging
import volaris
from api.characters import Characters

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

config = yaml.safe_load(open("./config.yml"))

token = config.get("token")

client = commands.Bot(
    command_prefix=config["prefix"]
)

characters = Characters()
@client.event
async def on_ready():
    glist = []
    for guild in client.guilds:
        glist.append(guild.id)
        print(guild.name)
    config["guild_ids"] = glist

    print("guild ids registered")

    with open(f"config.yml", "w") as f:
        yaml.dump(config, f)
        print("config saved")
    
    print("cogs loaded")

    print(f"logged in as {client.user}")


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        print(filename)
        client.load_extension(f'cogs.{filename[:-3]}')



client.run(token)
