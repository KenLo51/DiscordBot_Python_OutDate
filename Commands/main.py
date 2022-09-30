import discord#discord.py==1.3.3
from discord.ext import commands

class main(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def ping(self, ctx):
		latency = self.bot.latency*1000#ms
		await ctx.send("%7.2fms"%(latency))

	@commands.command()
	async def mainHelp(self, ctx):
		await ctx.send("""ping: Return the latency of the bot receive message.""")

def setup(bot):
	bot.add_cog(main(bot))