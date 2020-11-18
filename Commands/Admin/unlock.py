import discord
from discord.ext import commands
from discord.utils import get
import json
import os
class MyCog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command()
    async def unlock(self,ctx):
        os.getcwd()
        file = json.load(open("roles.json","r"))
        moderatorRoleIDs = file["admin"]
        usr = ctx.author
        rls = usr.roles
        grls = ctx.guild.default_role
        for rl in rls:
            if str(rl.id) in moderatorRoleIDs:
                channel = ctx.channel
                await channel.set_permissions(grls,send_messages=True)
                await ctx.send("Channel Unlocked")
                return None
        await ctx.send("You cant do that noob!")