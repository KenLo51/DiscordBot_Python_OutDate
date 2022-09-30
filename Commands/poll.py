import discord#discord.py==1.3.3
from discord.ext import commands
from Commands.poll import poll_control
class poll(commands.Cog):
#poll data format:
#{<guild_id>:{	"title" : <str>,
#						"comment" : <str>,
#						"date" : {"start" : <str>, "end" : <str>},
#						"author_id" : <int>,
#						"channel_id" : <int>,
#						"data" : [	"id" : <int>,
#										"options" : <str>,
#										"voters" : [<id>, <id>, ...],
#					}
#}

	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def poll(self, ctx):
		#poll <title> c<comment> <option>
		print('poll called')

	@commands.command()
	async def poll_edit(self, ctx, mode):
		print('poll_edit called')
		if(mode=="add"):
			return
		if(mode=="del"):
			return
		if(mode=="title"):
			return
		if(mode=="comment"):
			return
		if(mode=="date"):
			return



def setup(bot):
	bot.add_cog(poll(bot))