import discord#discord.py==1.3.3
from discord.ext import commands
from Commands.poll import poll_control
class compiler(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def cpp(self, ctx):
		#c++ compiler
		print('poll called')

	@commands.command()
	async def python3(self, ctx):
		#c++ compiler
		print('poll called')



def setup(bot):
	bot.add_cog(compiler(bot))