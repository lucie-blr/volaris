import discord
from discord.ext import commands
from discord.commands import Option, SlashCommandGroup
import yaml, os
import api.character
from api.race import *
from main import characters, config

class Character(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    cmd = SlashCommandGroup("character", "Commands for character!")
    management = cmd.create_subgroup("management", "Commands for characters management.")

    Race_ids = []
    for filename in os.listdir('./database/Races'):
        if filename.endswith('.yml'):
            print(filename)
            Race_ids.append(filename[:-4])
    Classe_ids = []
    for filename in os.listdir('./database/Classes'):
        if filename.endswith('.yml'):
            print(filename)
            Classe_ids.append(filename[:-4])
    Faction_ids = []
    for filename in os.listdir('./database/Factions'):
        if filename.endswith('.yml'):
            print(filename)
            Faction_ids.append(filename[:-4])
            
    @management.command(   guild_ids = config.get("guild_ids"),
                    name = "get_loaded",
                    usage = "",
                    description = "description")
    async def get_loaded(self, ctx):
        await ctx.respond(f"Loaded {characters.get_characters_by_names()}.", ephemeral=True)

    @cmd.command(
                    guild_ids = config.get("guild_ids"),
                    name = "load",
                    usage="",
                    description = "description")
    async def load(self, ctx):
        if (ctx.author.id in characters.get_characters_by_ids()):
            await ctx.respond("You already loaded you're character.")
            return

        character = api.character.Character(ctx.author.id)
        await ctx.respond(f"Character {character.name} succesfully loaded.")
        characters.add_character(character)

    @cmd.command(
                    guild_ids = config.get("guild_ids"),
                    name = "create",
                    usage="<name> <>",
                    description = "description")
    async def create(self, ctx, 
    name:str, 
    age:int, 
    sexe: Option(str, "Sexe", choices=["male", "female"], required=True),
    race_id: Option(str, "Race", choices=Race_ids, required=True),
    classe_id: Option(str, "Classe", choices=Classe_ids, required=True),    
    faction_id: Option(str, "Faction", choices=Faction_ids, required=True)):
        data = {
            'name': name,
            'age': age,
            'sexe': sexe,
            'race': race_id,
            'classe': classe_id,
            'classe_2': None,
            'faction_id': faction_id,
            'level': 1,
            'xp': 0,
            'hp': 10,
            'zone': 'spawn',
            'team': None,
            'atk': 5}

        if os.path.exists(f"./database/characters/{ctx.author.id}.yml"):
            await ctx.respond("You already got a character !")
        else:
            with open(f"database/characters/{ctx.author.id}.yml", "w") as f:
                yaml.dump(data, f, default_flow_style=False)
            await ctx.respond("Character created !")    

    

def setup(bot:commands.Bot):
        bot.add_cog(Character(bot))