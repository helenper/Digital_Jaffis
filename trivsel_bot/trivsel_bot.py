import discord
import os

from discord.ext import commands

admin_roles = ["Utvalg","Frivillig","Trivselsteam","Systemadministrator"]

client = commands.Bot(command_prefix = "!")
#client.remove_command("help")

@client.event
async def on_ready():
    print("Yeey, I'm online!")

@client.command(hidden=True)
@commands.has_role("Systemadministrator")
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")

@client.command(hidden=True)
@commands.has_role("Systemadministrator")
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")

@client.command(hidden=True)
@commands.has_role("Systemadministrator")
async def reload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    client.load_extension(f"cogs.{extension}")


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")


#Insert your own token here
client.run("Token")
