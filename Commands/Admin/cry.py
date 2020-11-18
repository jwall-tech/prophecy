import discord
from discord.ext import commands
from discord.utils import get
import json
import os
class MyCog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command()
    async def prophecy(self,ctx):
        if ctx.author.id == 484155513915965452:
            await ctx.send("Hi master, what is it you desire?")