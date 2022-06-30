import discord
from discord.ext import commands

import json
from discord.ext.commands.core import command
import requests

class Action(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command()
    async def wink(self, ctx, member: discord.Member = None):

        api = 'https://some-random-api.ml/animu/wink'
        json_data = requests.get(api).json()
        image = json_data["link"]

        if member == None:

            embed = discord.Embed(title=ctx.author.name + " is winking", colour=discord.Colour.blue())
            embed.set_image(url= image)

            await ctx.send(embed=embed)

            return

        embed = discord.Embed(title=ctx.author.name + " winks at " + member.name,
        colour=discord.Colour.blue())
        embed.set_image(url= image)

        await ctx.send(embed=embed)

    @commands.command()
    async def pat(self, ctx, member: discord.Member):
        
        api = 'https://some-random-api.ml/animu/pat'
        json_data = requests.get(api).json()
        image = json_data["link"]

        embed = discord.Embed(title=ctx.author.name + " pats " + member.name,
        colour=discord.Colour.blue())
        embed.set_image(url= image)
    
        await ctx.send(embed=embed)

    @commands.command()
    async def hug(self, ctx, member: discord.Member):
        
        api = 'https://some-random-api.ml/animu/hug'
        json_data = requests.get(api).json()
        image = json_data["link"]

        embed = discord.Embed(title=ctx.author.name + " hugs " + member.name,
        colour=discord.Colour.blue())
        embed.set_image(url= image)
    
        await ctx.send(embed=embed) 


def setup(client):
    client.add_cog(Action(client))