import discord#discord.py==1.3.3
from discord.ext import commands
import json
class react(commands.Cog):
	def ReactDataSave(self):
		with open(self.jsonFn, mode='w') as f:
			f.write(json.dump(self.data))

	def __init__(self, bot, jsonDataFilename = 'reactData.json'):
		self.bot = bot
		self.jsonFn=jsonDataFilename
		try:
			with open(self.jsonFn, mode='r') as f:
				self.data = json.load(f)
		except:
			self.data = []

	@commands.command()
	async def addreact(self, ctx, tri, rct, equally):
		if(equally == "T"):
			equally="T"
		else:
			equally="F"
		self.data.append([tri, rct, equally])
		ReactDataSave()
		if(equally == "T"):
			await ctx.send(f'bot will send "{rct}" while "{tri}" in message')
		else:
			await ctx.send(f'bot will send "{rct}" while message is equal to "{tri}"')


	@commands.command()
	async def delreact(self, ctx, tri, rct, equally):
		if(equally == "T"):
			equally="T"
		else:
			equally="F"
		try:
			self.data.remove([tri, rct, equally])
			ReactDataSave()
			await ctx.send("reaction has removed")
		except:
			await ctx.send("No match found")

	@commands.Cog.listener()
	async def on_message(self, message):
		if(message.author == self.bot.user):
			return
		msgtext = message.content
		for data in self.data:
			if(data[2] == "T"):
				if(data[0] == msgtext):
					await message.send(data[1])
					return
			elif(data[2] == "F"):
				if(data[0] in msgtext):
					await message.send(data[1])
					return
		print(message.content)
		print(message.application)

def setup(bot):
	bot.add_cog(react(bot))
