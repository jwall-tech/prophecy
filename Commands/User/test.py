import discord
from discord.ext import commands

class MyCog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command()
    async def test(self,ctx):
        usr = ctx.author
        if usr.id == 742212377990135819:
            await ctx.send("die")
        else:
            await ctx.send("wow you are smart!")