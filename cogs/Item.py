import discord
from discord.ext import commands
from discord.commands import Option, SlashCommandGroup

from main import config

import api.item

class Item(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    cmd = SlashCommandGroup("items", "Commands for items")
    management = cmd.create_subgroup("management", "Commands for items management.")


    @management.command(   guild_ids = config.get("guild_ids"),
                    name = "create",
                    usage = "",
                    description = "description")
    async def create(self, ctx, 
    name: str,
    id:str, 
    type_id:str,
    bonus: str,
    effect: str
    ):
        """
        Create a new item."""

        try:
            if os.path.exists(f"./database/Items/{type_id}/{ctx.author.id}.yml"):
                await ctx.respond("This item already exist!")
                return
        except:
            pass

        it = api.item.Item()
        it.create(name, id, type_id, bonus, effect)
        it.save()
        await ctx.respond(f"Item {it.get_id()} created!")
                
def setup(bot:commands.Bot):
        bot.add_cog(Item(bot))
