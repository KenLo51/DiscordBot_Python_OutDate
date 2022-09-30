##########################discord library
import discord#discord.py==1.3.3
from discord.ext import commands

##########################python library
import asyncio

##########################custome library
from Commands.terminal_module import terminal_control

class terminal(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.terminal = None

	@commands.command()
	async def open_terminal(self, ctx):
		print("open a terminal on",ctx.channel.id)
		terminal = terminal_control.terminal_control()
		self.terminal = {ctx.channel.id : terminal}
		print_data = ''
		while(True):
			await asyncio.sleep(0.5)
			data = terminal.getdata()
			print_data = print_data + data
			if(data != ''):
				break
		await ctx.send("```"+print_data+"```")

	@commands.command()
	async def close_terminal(self, ctx):
		terminal = None
		try:
			terminal = self.terminal[ctx.channel.id]
		except:
			return
		terminal.close()
		self.terminal.pop(ctx.channel.id)
		await ctx.send("Terminal Closed")

	@commands.Cog.listener()
	async def on_message(self, ctx):
		if(ctx.author.id == 725255298897412117):
			return
		if(ctx.content[0:2]!='>>'):
			return
		terminal = None
		try:
			terminal = self.terminal[ctx.channel.id]
		except:
			return
		print("terminal command", ctx.content, "on", ctx.channel.id)
		terminal.writedata(ctx.content[2:])
		print_data = ''
		while(True):
			await asyncio.sleep(0.5)
			data = terminal.getdata()
			print_data = print_data + data
			if(data != ''):
				break
		print("print_data", print_data)
		print_data = print_data.replace("```", "'''")
		print_data = print_data.replace(ctx.content[2:], "", 1)
		print_data = print_data.split('\n')
		for index in range(0, len(print_data), 20):
			print_string = "\n"
			for data in print_data[index: (index+20 or len(print_data))]:
				print_string = print_string + data
			await ctx.channel.send("```"+print_string+"```")


def setup(bot):
	bot.add_cog(terminal(bot))