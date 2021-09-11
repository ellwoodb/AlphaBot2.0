import os
import discord
from discord.ext import commands, tasks
from itertools import cycle

from discord.ext.commands.errors import CommandNotFound, MissingRequiredArgument


intents = discord.Intents.all()
client = commands.Bot(command_prefix="..", intents=intents)
precense_text = "in testing..."


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(precense_text))
    print("READY!")


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        ctx.send("This command wasn't found.")
    else:
        print(f"Error: '{error}'")


@client.command()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")
    print(f"Loaded cog {extension}.")
    await ctx.send(f"Loaded cog {extension}.")


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    print(f"Unloaded cog {extension}.")
    await ctx.send(f"Unloaded cog {extension}.")


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")
        print(f"Loaded Cog: [{filename[:-3]}]")

token = open("token", "r")
client.run(token.read())
