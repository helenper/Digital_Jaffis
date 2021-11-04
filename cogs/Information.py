import discord
import random

from discord.ext import commands

admin_roles = ["Utvalg","Frivillig","Trivselsteam","Systemadministrator"]

class Information(commands.Cog):

    def __init__ (self, client):
        self.client = client

    @commands.command(hidden=True)
    @commands.has_any_role(*admin_roles)
    async def snart_natta(self, ctx):
        await ctx.send(f"Det er på tide å ta kvelden. Discord serveren vil snart bli stengt. Vi vil være tilbake igjen klokken 10.00 i morgen. Håper vi sees da!")

    @commands.command(hidden=True)
    @commands.has_any_role(*admin_roles)
    async def natta(self, ctx):
        await ctx.send(f"Discord serveren er nå stengt for natten. Vi er tilbake klokken 10.00 i morgen. ")

        #await guild.channel.set_permissions(guild.Deltager, send_messages=False)




def setup(client):
    client.add_cog(Information(client))
