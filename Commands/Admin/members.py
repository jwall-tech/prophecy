import discord
from discord.ext import commands
from discord.utils import get
import json
import os
class MyCog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command()
    async def members(self,ctx):
        os.getcwd()
        file = json.load(open("roles.json","r"))
        moderatorRoleIDs = file["admin"]
        usr = ctx.author
        rls = usr.roles
        grls = ctx.guild.default_role
        for rl in rls:
            if str(rl.id) in moderatorRoleIDs:
                await ctx.send("Member Count Coming...")
                await ctx.send("Calculating")
                membcount = 0
                for _ in ctx.guild.members:
                    membcount += 1
                await ctx.send("Member Count is "+str(membcount))
                return None
        await ctx.send("You cant do that noob!")