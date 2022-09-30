import discord#discord.py==1.3.3
from discord.ext import commands
import requests



class NSFW(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def 開車(self, ctx):
		await ctx.send()

	@commands.command()
	async def NSFWHelp(self, ctx):
		await ctx.send("""NULL""")

def setup(bot):
	bot.add_cog(NSFW(bot))