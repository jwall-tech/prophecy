import discord
from discord.ext import commands
from discord.utils import get
import json
import os
class MyCog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command()
    async def ban(self,ctx,user: discord.Member):
        os.getcwd()
        file = json.load(open("roles.json","r"))
        moderatorRoleIDs = file["mod"]
        usr = ctx.author
        rls = usr.roles
        for rl in rls:
            if str(rl.id) in moderatorRoleIDs:
                if user:
                    await user.ban()
                    await ctx.send("User: "+user.display_name+" was banned xd lol")
                else:
                    await ctx.send("mention a user plz <3 (.kick @BigBean)")
                return None
        await ctx.send("You cant do that noob!")