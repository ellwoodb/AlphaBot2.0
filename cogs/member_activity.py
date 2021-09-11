import discord
from discord.ext import commands


class MemberActivity(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        server = member.guild
        print(f"'{member}' joined '{server}'.")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        server = member.guild
        print(f"'{member}' left '{server}'.")


def setup(client):
    client.add_cog(MemberActivity(client))
