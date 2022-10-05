import discord
from discord.ext import commands
import yaml

class Test(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
        
    config = yaml.safe_load(open("config.yml"))

    @commands.slash_command(
                    guild_ids = config.get("guild_ids"),
                    name = "test",
                    usage="<usage>",
                    description = "description")
    @commands.guild_only()
    @commands.has_permissions()
    async def test(self, ctx):
        await ctx.respond("template command")


def setup(bot:commands.Bot):
    bot.add_cog(Test(bot))