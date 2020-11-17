import discord
from discord.ext import commands
from discord.utils import get
import json
import os
class MyCog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command()
    async def mute(self,ctx,user: discord.Member):
        os.getcwd()
        file = json.load(open("roles.json","r"))
        moderatorRoleIDs = file["mod"]
        usr = ctx.author
        rls = usr.roles
        grls = ctx.guild.roles
        for rl in rls:
            if str(rl.id) in moderatorRoleIDs:
                if user and get(grls,name="Muted"):
                    role = get(grls,name="Muted")
                    await user.add_roles(role)
                    await ctx.send("xd dude got muted lol ("+user.display_name+")")
                else:
                    await ctx.send("mention a user plz <3 (.kick @BigBean)")
                return None
        await ctx.send("You cant do that noob!")