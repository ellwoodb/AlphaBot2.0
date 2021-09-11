import discord
from discord.ext import commands
from discord.ext.commands.errors import MissingAnyRole, MissingPermissions, MissingRequiredArgument


class Kick(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f"Kicked {member.mention}. Reason: {reason}")

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, MissingRequiredArgument):
            await ctx.send("Please provide a member to kick.")
        elif isinstance(error, MissingPermissions):
            await ctx.send("You are not allowed to do that.")


def setup(client):
    client.add_cog(Kick(client))
