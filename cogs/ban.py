import discord
from discord.ext import commands
from discord.ext.commands.errors import MissingAnyRole, MissingPermissions, MissingRequiredArgument


class Ban(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f"Banned {member.mention}. Reason: {reason}")

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, MissingRequiredArgument):
            await ctx.send("Please provide a member to ban.")
        elif isinstance(error, MissingPermissions):
            await ctx.send("You are not allowed to do that.")



def setup(client):
    client.add_cog(Ban(client))
