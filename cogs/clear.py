import discord
from discord.ext import commands
from discord.ext.commands.errors import MissingPermissions, MissingRequiredArgument


class Clear(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        if amount == 0:
            await ctx.send("Amount can't be 0.")

        await ctx.channel.purge(limit=amount+1)

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, MissingRequiredArgument):
            await ctx.send("Please specify an amount of messages to clear.")
        elif isinstance(error, MissingPermissions):
            await ctx.send("You are not allowed to do that.")


def setup(client):
    client.add_cog(Clear(client))
