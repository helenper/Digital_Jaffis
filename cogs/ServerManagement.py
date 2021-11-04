import discord
import shlex

from discord.ext import commands
from discord.utils import get

admin_roles = ["Utvalg","Frivillig","Trivselsteam","Systemadministrator"]
bad_words = ["Onlyfans",
"pornhub",
"onlyfans",
"onlyfans.com",
"0nlyfans",
"heroin",
"hasj",
"weed",
"WEED",
"Weed",
"W33d",
"w33d",
"W33D",
"amf",
"amfetamin",
"amfetmin",
"speed",
"coke",
"mdma",
"ma",
"ecstesy",
"kokain",
"crack",
"cannabis",
"canabis",
"ghb",
"transe",
"shemale",
"hore",
"neger",
"nigger",
"hora",
"horen",
"horer",
"horene",
"horebukk",
"horebukken",
"horebukker",
"horebukkene",
"ronk",
"ronken",
"ronket",
"ronke",
"ronker",
"ronka",
"ronking",
"runk",
"runke",
"runken",
"runket",
"runker",
"runka",
"runking",
"nigger",
"niggeren",
"niggere",
"niggerne",
"pakkis",
"pakkisen",
"pakkiser",
"pakkisene",
"svarting",
"svartingen",
"svartinger",
"svartingene",
"sotrør",
"sotrøret",
"sotrørene",
"sotror",
"sotroret",
"sotrorene",
"sotroer",
"sotroeret",
"sotroerene",
"barneporno",
"barnepornografi",
"pedofil",
"pedofile",
"pedofili",
"pedo",
"quisling",
"vidkun-quisling",
"vidkunquisling",
"hitler",
"adolfhitler",
"adolf-hitler",
"sieg-heil",
"siegheil",
"heil-hitler",
"heilhitler",
"der-fuhrer",
"derfuhrer",
"1488",
"hvitmakt",
"whitepower",
"lesbesatan",
 ]

d_names_and_nicks = {}
f = open("names_to_nicknames.txt", "r")
for line in f.readlines():
        d_name, d_nick = line.split("&")
        d_names_and_nicks[d_name] = d_nick

f.close()


#print(f"{d_names_and_nicks}")

class ServerManagement(commands.Cog):

    def __init__ (self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Yeey, I'm online!")


    @commands.Cog.listener()
    async def on_member_join(self, member):
        n = d_names_and_nicks[f"{member.name}#{member.discriminator}"]

        try:
            await member.edit(nick=n)
            print(f"{member} was given nickname {n}")

            role = get(member.guild.roles, name="Deltager")
            await member.add_roles(role)
            print(f"{member} was given role {role}")

            for channel in member.guild.channels:
                if str(channel) == "innsjekk": # We check to make sure we are sending the message in the general channel
                    await channel.send(f"""Velkommen til serveren {member.mention}""")

        except:
            print(f"{member} was NOT given nickname {n} and new role. Check if {member} is \
            registered to camp or if something is wrong with given discord \
            name or discord nickname")

        """
        # Keep just in case of fire!! The code below works!

        for channel in member.guild.channels:
            #print(f"{channel}")
            if str(channel) == "innsjekk": # We check to make sure we are sending the message in the general channel
                await channel.send(f"Velkommen til serveren {member.mention}")

        role = get(member.guild.roles, name="Deltager")
        await member.add_roles(role)
        print(f"{member} was given role {role}")

        n = d_names_and_nicks[f"{member.name}#{member.discriminator}"]

        try:
                await member.edit(nick=n)
                print(f"{member} was given nickname {n}")
        except:
                print(f"{member} was NOT given nickname {n}. Check if {member} is \
                registered to camp or if something is wrong with given discord \
                name or discord nickname")
        """



    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f"{member} has left a server.")


    @commands.Cog.listener()
    async def on_message(self, message):
        split = shlex.split(message.content.lower())
        print(f"{split}")
        for word in split:
            #print(word)
            if word in bad_words:
                #print(f"Heeelo")
                await message.delete()
                await message.channel.send("Meldingen ble slettet")
                print(f"Message:{message.created_at} {message} from user {message.author} was deleted")

                logfile = open("logfil_deleted_messages.txt", "a+")
                logfile.write(f"{message.created_at} Message from user {message.author}: {split} - {message} was deleted \n")
                logfile.write("\n")
                logfile.close()

        #print(f"{word} for {word} in {bad_words}")
        #if any(word for word in bad_words if word in split):
        #if any(substring for bad in bad_words for substring in split if bad in substring):

            # rewrite

            #await send("Meldingen ble slettet")

            # async
            #await message.delete_message(message)

    @commands.command(hidden=True)
    @commands.has_any_role("Systemadministrator")
    #@commands.has_permissions(manage_messages=True)
    async def ping(self, ctx):
        await ctx.send(f"Pong! {round(self.client.latency * 1000)} ms")


    @commands.command(hidden=True)
    #@commands.has_permissions(manage_messages=True)
    @commands.has_any_role(*admin_roles)
    async def clear(self, ctx, amount=2):
        await ctx.channel.purge(limit=amount)


    @commands.command(hidden=True)
    @commands.has_any_role(*admin_roles)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)

    @commands.command(hidden=True)
    @commands.has_any_role(*admin_roles)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await send(f"Banned {member.mention}")

    """
    @commands.command(hidden=True)
    @commands.has_any_role(*admin_roles)
    async def unban(self, ctx, *, member):
        banned_user = await ctx.guild.bans()
        print(f"{banned_user.name}")
        member_name,  member_discriminator = self.member.split("#")

        for ban_entry in ban_user:
            user = ban_entry.user
            print(f"user {user}")

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                #await ctx.send(f"Unbanned {user.name}#{user.discriminator}")
                await ctx.send(f"Unbanned {user.mention}")
                return
    """

    @commands.command(hidden=True)
    async def on_message_deleted(self, message):
        await self.client.send_message(message.channel, "Message deleted.")



def setup(client):
    client.add_cog(ServerManagement(client))
