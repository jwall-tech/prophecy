import discord
from discord.ext import commands
from discord.utils import get
import json
import os
class MyCog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command()
    async def setup(self,ctx):
        os.getcwd()
        file = json.load(open("roles.json","r"))
        moderatorRoleIDs = file["mod"]
        channels = ctx.guild.channels
        usr = ctx.author
        grls = ctx.guild.roles
        rls = usr.roles
        for rl in rls:
            if str(rl.id) in moderatorRoleIDs:
                for chan in channels:
                    role = get(grls,name="Muted")
                    await chan.set_permissions(role,send_messages=False)
                return None
        await ctx.send("You cant do that noob!")