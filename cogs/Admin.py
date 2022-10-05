import discord
from discord.ext import commands
import yaml

class Admin(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    config = yaml.safe_load(open("config.yml"))

    @commands.slash_command(guild_ids=config.get("guild_ids"),
                    name = "set_admin",
                    usage="<usage>",
                    description = "description")
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def set_admin(self, ctx, role : discord.Role = None):
        config = yaml.safe_load(open("config.yml"))
        
        if role == None:
            await ctx.respond("Vous devez mentionner le rôle à passer administrateur bot", ephemeral=True)
            return

        if config["administrators"] == role.id:
            await ctx.respond("Le rôle est déjà administrateur bot", ephemeral=True)
            return

        else:
            config["administrators"] = role.id
            await ctx.respond("Le rôle a été défini comme administrateur bot")
            with open(f"config.yml", "w") as f:
                yaml.dump(config, f)
                print("config saved")


    @commands.slash_command(guild_ids = config.get("guild_ids"),
                    name = "set_mod",
                    usage="<usage>",
                    description = "description")
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def set_mod(self, ctx, role : discord.Role = None):
        config = yaml.safe_load(open("config.yml"))
        
        if role == None:
            await ctx.respond("Vous devez mentionner le rôle à passer administrateur bot", ephemeral=True)
            return

        if config["moderators"] == role.id:
            await ctx.respond("Le rôle est déjà modérateur bot", ephemeral=True)
            return

        else:
            config["moderators"] = role.id
            await ctx.respond("Le rôle a été défini comme modérateur bot")
            with open(f"config.yml", "w") as f:
                yaml.dump(config, f)
                print("config saved")


def setup(bot:commands.Bot):
    bot.add_cog(Admin(bot))