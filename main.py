import discord
from discord.ext import commands

import asyncio
import os
import random
token = "your token"
client = commands.Bot(command_prefix="s!")
client.remove_command("help")

@client.event
async def on_ready():
	print("bot is ready")


async def ch_pr():
	await client.wait_until_ready()

	statuses = ["with you", "s!help", "in Isle", ]

	while not client.is_closed():

		status = random.choice(statuses)
		await client.change_presence(activity=discord.Game(name=status))

		await asyncio.sleep(30)


client.loop.create_task(ch_pr())


#cogs======= 

@client.command()
@commands.is_owner()
async def load(ctx, extension):
	client.load_extension(f'cogs.{extension}')

	await ctx.send(f'{extension} has loaded')

@client.command()
@commands.is_owner()
async def unload(ctx, extension):
	client.unload_extension(f'cogs.{extension}')
	await ctx.send(f'{extension} has unloaded')

@client.command()
@commands.is_owner()
async def reload(ctx, extension):
	client.unload_extension(f'cogs.{extension}')
	client.load_extension(f'cogs.{extension}')
	await ctx.send(f'{extension} has reloaded')

for filename in os.listdir('/cogs'):
	if filename.endswith('.py'):
		client.load_extension(f'cogs.{filename[:-3]}')


client.run(token)
