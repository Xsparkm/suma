import discord
from discord.ext import commands
from discord import app_commands

import asyncio
import os
from os import environ
from dotenv import load_dotenv

load_dotenv()
TOKEN = environ["TOKEN"]

client = commands.Bot(command_prefix="!",intents=discord.Intents.all())
client.remove_command('help')

@client.event
async def on_ready():
  print('Bot is online')
  try:
      synced = await client.tree.sync()
      print(f'synced {len(synced)} command')
  except Exception as e:
    print(e)

  

@client.tree.command(description='says the owner name')
async def owner(interaction: discord.Interaction):
    await interaction.response.send_message("sparkm")

'''#load cogs
async def load_extensions():
    for filename in os.listdir("/cogs"):
        if filename.endswith(".py"):
            # cut off the .py from the file name
            await client.load_extension(f"cogs.{filename[:-3]}")


'''
async def main():
    async with client:
        # await load_extensions()
        await client.start(TOKEN)

asyncio.run(main())
