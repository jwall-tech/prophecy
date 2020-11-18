import discord
from discord.ext import commands
import json
import os

class MyCog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command()
    async def test2(self,ctx):
        os.getcwd()
        file = json.load(open("roles.json","r"))
        moderatorRoleIDs = file["mod"]
        print(moderatorRoleIDs)
        usr = ctx.author
        rls = usr.roles
        for rl in rls:
            if str(rl.id) in moderatorRoleIDs:
                await ctx.send("nice!")
                return None
        await ctx.send("You cant do that noob!")