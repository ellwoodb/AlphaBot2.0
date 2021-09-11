import discord
from discord.ext import commands


class Unban(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def unban(self, ctx, *, member: discord.Member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.banned_users

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.channel.send(f"Unbanned {user.mention}.")
                return


def setup(client):
    client.add_cog(Unban(client))
