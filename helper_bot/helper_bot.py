import discord
import os

from discord.ext import commands

admin_roles = ["Utvalg","Frivillig","Trivselsteam","Systemadministrator"]

client = commands.Bot(command_prefix = "!")
#client.remove_command("help")

@client.command(hidden=True)
@commands.has_permissions(manage_messages=True)
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")

@client.command(hidden=True)
@commands.has_permissions(manage_messages=True)
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")

@client.command(hidden=True)
@commands.has_permissions(manage_messages=True)
async def reload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    client.load_extension(f"cogs.{extension}")

"""
@client.command(hidden=True,pass_context=True)
@client.has_any_role("Deltager")
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        discord.Colour.orange()
    )

    embed.set_author(name="Help")
        embed.set_field(nam)
"""

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")


# Insert your own token below
client.run("Token")


"""
# The following piece of code works
# NB: Must move client.run below

@client.event
async def on_ready():
    print("Yeey, I'm online!")

@client.event
async def on_member_join(member):
    print(f"{member} has joined a server.")

@client.event
async def on_member_remove(member):
    print(f"{member} has left a server.")

@client.command()
async def ping(ctx):
     await ctx.send(f"Pong! {round(client.latency * 1000)} ms")

@client.command(aliases=["8ball"])
async def _8ball(ctx, *, question):

    responses = ["As I see it, yes.",
                 "Ask again later.",
                 "Better not tell you now.",
                 "Cannot  predict now.",
                 "Concentrate and ask again.",
                 "Don’t count on it.",
                 "It is certain.",
                 "It is decidedly so.",
                 "Most likely.",
                 "My reply is no.",
                 "My sources say no.",
                 "Outlook not so good.",
                 "Outlook good.",
                 "Reply hazy, try again.",
                 "Signs point to yes.",
                 "Very doubtful.",
                 "Without a doubt.",
                 "Yes.",
                 "Yes – definitely.",
                 "You may rely on it.",
                 ]
    await ctx.send(f"Question: {question}\n Answer: {random.choice(responses)}")

@client.command()
async def clear(ctx, amount=2):
    await ctx.channel.purge(limit=amount)


@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await send(f"Banned {member.mention}")

@client.command()
async def unban(ctx, *, member):
    banned_user = await ctx.guild.bans()
    member_name,  member_discriminator = member.split("#")

    for ban_entry in ban_user:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"Unbanedn {user.name}#{user.discriminator}")

            return
"""
