import os
import asyncio,random,time
import discord#discord.py==1.3.3
from discord.ext import commands
import socket,math

import FileRW

#########################################################global variable define
polls=[]#polls data
isBuilding = False

#########################################################read confing
config = FileRW.readConfig('DiscordBotConfig.ini')
emoji = FileRW.readEmoji()

#########################################################bot init
intents = discord.Intents.all()
bot = commands.Bot(command_prefix = config['prefix'])

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command()
async def load(ctx, ExtensionName):
    try:
        bot.load_extension(f"Commands.{ExtensionName}")
        await ctx.send(f"{ExtensionName} has loaded")
    except:
        await ctx.send(f"{ExtensionName} not found")

@bot.command()
async def loadAll(ctx):
    categorys = FileRW.readCategory('Commands_Category.json')
    success_categorys = []
    failed_categorys = []
    for category in categorys:
        try:
            bot.load_extension(f"Commands.{category}")
            success_categorys.append(category)
        except:
            failed_categorys.append(category)

    if(len(success_categorys)>0):
        categorys_string = " , ".join(success_categorys)  
        await ctx.send(f"{categorys_string} has loaded")
    if(len(failed_categorys)>0):
        categorys_string = " , ".join(failed_categorys)  
        await ctx.send(f"{categorys_string} has failed")



@bot.command()
async def unload(ctx, ExtensionName):
    try:
        r=bot.unload_extension(f"Commands.{ExtensionName}")
        await ctx.send(f"{ExtensionName} has removed")
    except:
        await ctx.send(f"{ExtensionName} not found")

@bot.command()
async def reload(ctx, ExtensionName):
    try:
        bot.reload_extension(f"Commands.{ExtensionName}")
        await ctx.send(f"{ExtensionName} has reloaded")
    except:
        await ctx.send(f"{ExtensionName} not found")



@bot.command()
async def status(ctx):
    global bootDate
    def sec2str(time):
        day = math.floor( time/(60*60*24) )
        time = time - (60*60*24)*day
        hour = math.floor( time/(60*60) )
        time = time - (60*60)*hour
        min = math.floor( time/(60) )
        time = time - (60)*min
        sec = math.floor(time)
        return(f"{day}days {hour}:{min}:{sec}")
    hostname = socket.gethostname()
    Time=sec2str(time.time() - bootDate)
    latency=int(bot.latency*1000)
    msg=f"""```
Running on: {hostname}
Online Time:    {Time}
Latency:        {latency}ms
```"""
    await ctx.send(msg)




#for file in os.listdir("./Commands"):
#    if(file.endswith(".py")):
#        bot.load_extension(f"Commands.{file[:-3]}")


bootDate = time.time()
bot.run(config['Token'])