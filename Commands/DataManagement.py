import discord#discord.py==1.3.3
from discord.ext import commands

import os


class DataManagement(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def list(self, ctx):
		UserID = str(ctx.author.id)
		dirData = os.listdir(f"ClientData")
		if( dirData.count( UserID ) == 0):
			os.mkdir(f"ClientData\{UserID}")
		dirData = os.listdir(f"ClientData\{UserID}")
		str1 = ''
		if(len(dirData) == 0):
			str1 = "No file in folder"
		else:
			str1 = '\n'.join(dirData)
		await ctx.send( str1 )


def setup(bot):
	bot.add_cog(DataManagement(bot))