import discord
from discord.ext import commands
from importlib import import_module
import os

Token = "Nzc4MzIzODMxMDg1NDY1NjMw.X7QUjQ.MeB9cPbb8qIX402rZ5giO5wix0w"

bot = commands.Bot(command_prefix=".")

mainPath = "Commands"

cmdsTAB = {}

dirs = os.listdir(mainPath)
for catagory in dirs:
    cmdsTAB[catagory] = []
    newdir = os.listdir(mainPath+"/"+catagory)
    for file in newdir:
        newpath = mainPath+"/"+catagory
        if not file.endswith('__'):
            finalpath = mainPath+"."+catagory+"."+file
            finalpath = finalpath[:-len(".py")]
            mod = import_module(finalpath)
            bot.add_cog(mod.MyCog(bot))

            cmdsTAB[catagory].append(file)

async def on_command_error(self,ctx,error=""):
    pass

bot.add_listener(on_command_error)

bot.run(Token)
