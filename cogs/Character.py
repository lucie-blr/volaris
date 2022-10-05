import discord
from discord.ext import commands
from discord.commands import Option
import yaml, os
from api.character import *
from api.race import *




class Character(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    config = yaml.safe_load(open("config.yml"))

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
            

    @commands.slash_command(
                    guild_ids = config.get("guild_ids"),
                    name = "create_character",
                    usage="<name> <>",
                    description = "description")
    @commands.guild_only()
    @commands.has_permissions()
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def create_character(self, ctx, 
    name:str, 
    age:int, 
    sexe: Option(str, "Sexe", choices=["male", "female"], required=True),
    race_id: Option(str, "Race", choices=Race_ids, required=True),
    classe_id: Option(str, "Classe", choices=Classe_ids, required=True)):
        await ctx.respond("template command")

        data = {
            'name': name,
            'age': age,
            'sexe': sexe,
            'race': race_id,
            'classe': classe_id,
            'level': 1,
            'xp': 0,
            'hp': 10,
            'zone': 'spawn',
            'stats': 00}

        
        character_id = "00"
        
        try:
            l = []
            for filename in os.listdir(f"database/characters/{ctx.author.id}"):
                l.append(filename[:-4])
            if len(l) >= 3:
                await ctx.send("Le joueur a atteint le nomber maximum de personnage")
                return
            else:
                if not "A" in l:
                    character_id = "A"
                    
                elif not "B" in l:
                    character_id = "B"
                    
                elif not "C" in l:
                    character_id = "C"
                    
            
            
        except FileNotFoundError:
            os.mkdir(f"database/characters/{ctx.author.id}")
            character_id = "01"
        
        with open(f"database/characters/{ctx.author.id}/{character_id}.yml", "w") as f:
            yaml.dump(data, f, default_flow_style=False)



def setup(bot:commands.Bot):
        bot.add_cog(Character(bot))