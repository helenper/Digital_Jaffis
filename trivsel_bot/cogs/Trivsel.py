import discord

from discord.ext import commands

admin_roles = ["Utvalg","Frivillig","Trivselsteam","Systemadministrator"]

class Trivsel(commands.Cog):

    def __init__ (self, client):
        self.client = client

    @commands.command(hidden=True)
    @commands.has_role("Systemadministrator")
    async def info_trivselbot_ny(self, ctx):

        role = ctx.guild.get_role

        for channel in ctx.guild.text_channels:
            #print(channel)


            if str(channel) == "generelt":

                await channel.send(f"Hei @everyone, Jeg er den nye trivselsboten! \n\nPer nå kan dere bruke meg til å sende en klem eller en high five til en annen deltaker. Spørre meg om å se inn i framtiden og få svar på noe du lurer på. \n\nJeg er helt ny og funker kanskje ikke helt optimalt enda, og det kan hende jeg lærer meg nye ting i løpet av leiren. Har du noen forslag til ting jeg kan lære meg, ta kontakt med de som har laget meg (aka Systemadministrator). \n\nMine kommandoer er: !klem @bruker, !high_five @bruker, og !8ball \"Ditt spørsmål\". \n\nHvis det dukker opp flere kommandoer vil du finne de ved å skrive !help")


    @commands.command()
    async def high_five(self, ctx, member : discord.Member):

        embed = discord.Embed(
            colour = discord.Colour.blue()
            )
        embed.add_field(name=f"{ctx.message.author.nick} sender en high five til {member.nick}" ,value=":smile:")

        await ctx.send(embed=embed)

        #await ctx.send(f"{ctx.message.author.nick} sender en high five til {member.nick}")

    @commands.command()
    async def klem(self, ctx, member : discord.Member):

        embed = discord.Embed(
                colour = discord.Colour.purple()
                )
        embed.add_field(name=f"{ctx.message.author.nick} sender en klem  til {member.nick}" ,value=":hugging:")

        await ctx.send(embed=embed)

        #await ctx.send(f"{ctx.message.author.nick} sender en klem  til {member.nick}")


def setup(client):
    client.add_cog(Trivsel(client))
