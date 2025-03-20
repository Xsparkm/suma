import discord
from discord.ext import commands

import json
import requests

class Sra(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['CAT'])
    async def cat(self,ctx):


        api = 'https://some-random-api.ml/img/cat'
        json_data = requests.get(api).json()
        image = json_data["link"]


        em = discord.Embed(description=":cat2: cat")
        em.set_image(url = image)

        await ctx.send(embed=em)


    @commands.command(aliases=['DOG'])
    async def dog(self,ctx):

        api = 'https://some-random-api.ml/img/dog'
        json_data = requests.get(api).json()
        image = json_data["link"]

        em = discord.Embed(description=":dog: dog")
        em.set_image(url = image)

        await ctx.send(embed=em)

    @commands.command(aliases=['PANDA'])
    async def panda(self,ctx):

        api = 'https://some-random-api.ml/img/panda'
        json_data = requests.get(api).json()
        image = json_data["link"]

        em = discord.Embed(description=":panda_face: panda")
        em.set_image(url = image)

        await ctx.send(embed=em)

    @commands.command(aliases=['BIRD'])
    async def bird(self,ctx):

        api = 'https://some-random-api.ml/img/birb'
        json_data = requests.get(api).json()
        image = json_data["link"]

        em = discord.Embed(description="🐦 bird")
        em.set_image(url = image)

        await ctx.send(embed=em)

    
    @commands.command(aliases=['FOX'])
    async def fox(self,ctx):

        api = 'https://some-random-api.ml/img/fox'
        json_data = requests.get(api).json()
        image = json_data["link"]

        em = discord.Embed(description="🦊 fox")
        em.set_image(url = image)

        await ctx.send(embed=em)

    @commands.command(aliases=['KOALA'])
    async def koala(self,ctx):

        api = 'https://some-random-api.ml/img/koala'
        json_data = requests.get(api).json()
        image = json_data["link"]

        em = discord.Embed(description="🐨 koala")
        em.set_image(url = image)

        await ctx.send(embed=em)



    @commands.command(aliases=['pokemon','dex'])
    async def pokedex(self,ctx, args = None):


        pokemon = args
        api = 'https://some-random-api.ml/pokedex?pokemon='+pokemon
        json_data = requests.get(api).json()
        name = json_data["name"]
        ids = json_data["id"]
        types = json_data["type"]
        spe = json_data["species"]
        image = json_data["sprites"]
        desc = json_data["description"]
        evolu = json_data['family']
        abily = json_data['abilities']
        H = json_data['height']
        W = json_data['weight']
        G = json_data['generation']
        gender = json_data['gender']
        stat = json_data['stats']



        s = ", "

        com = s.join(types)
        spes = s.join(spe)
        abi = s.join(abily)
        evo = s.join(evolu['evolutionLine'])
        gen = s.join(gender)

        em = discord.Embed(
          title =f"{name} #{ids}",
          description=f":robot: : **{desc}**",
          color = discord.Color.red()
        )

        em.set_thumbnail(
          url=image["animated"]
        )

        em.add_field(
          name="Types",
          value=f"{com}",
           
        )

        em.add_field(
          name="Species",
          value=f"{spes}",
           
        )

        em.add_field(
          name="Ability",
          value=f"{abi}",
           
        )

        em.add_field(
          name="Evolution Stage",
          value=f"The {evolu['evolutionStage']} Evolution",
           
        )

        em.add_field(
          name="Evolution Line",
          value=f"{evo}",
          inline=False
        )

        em.add_field(
          name="Height",
          value=f"{H}",
           
        )

        em.add_field(
          name="Weight",
          value=f"{W}",
           
        )

        em.add_field(
          name="Gender",
          value=f"{gen}",
           
        )

        em.add_field(
          name="Stats :",
          value=f":heart: : {stat['hp']}\n:crossed_swords: : {stat['attack']}\n:shield: : {stat['defense']}\n:dash: : {stat['speed']}",
          inline = True
        )

        em.add_field(
          name="Sp Stats :",
          value=f"Sp :crossed_swords: : {stat['sp_atk']}\nSp️ ️:shield: : {stat['sp_def']}",
          inline = True
        )

        em.set_footer(
          text=f"This Pokemon Is From The {G} Generation\nTotal Stats : {stat['total']}"
        )

        await ctx.send(embed=em)


    @commands.command(aliases=['memes'])
    async def meme(self,ctx):


      api = 'https://some-random-api.ml/meme'
      json_data = requests.get(api).json()
      name = json_data["image"]
      lol = json_data["caption"]


      em = discord.Embed(description=lol)
      em.set_image(url = name)

      await ctx.send(embed=em)

    @commands.command()
    async def glass(self, ctx, member: discord.Member = None):
        """Add a glass filter to a profile picture."""
        user = member or ctx.message.author
        av = str(user.avatar_url_as(format='png'))
        url = f'https://some-random-api.ml/canvas/glass?avatar={av}'
        embed = discord.Embed(color=0x5643fd, timestamp=ctx.message.created_at)
        embed.set_image(url=url)
        await ctx.send(embed=embed)

    @commands.command(aliases= ['rainbow'])
    async def gay(self, ctx, member: discord.Member = None):
        """Add a rainbow filter to a profile picture."""
        user = member or ctx.message.author
        av = str(user.avatar_url_as(format='png'))
        url = f'https://some-random-api.ml/canvas/gay?avatar={av}'
        embed = discord.Embed(color=0x5643fd, timestamp=ctx.message.created_at)
        embed.set_image(url=url)
        await ctx.send(embed=embed)

    @commands.command()
    async def invert(self, ctx, member: discord.Member = None):
        """Add an inverted filter to a profile picture."""
        user = member or ctx.message.author
        av = str(user.avatar_url_as(format='png'))
        url = f'https://some-random-api.ml/canvas/invert?avatar={av}'
        embed = discord.Embed(color=0x5643fd, timestamp=ctx.message.created_at)
        embed.set_image(url=url)
        await ctx.send(embed=embed)

    @commands.command()
    async def wasted(self, ctx, member: discord.Member = None):
        """Add a GTA V wasted filter to a profile picture."""
        user = member or ctx.message.author
        av = str(user.avatar_url_as(format='png'))
        url = f'https://some-random-api.ml/canvas/wasted?avatar={av}'
        embed = discord.Embed(color=0x5643fd, timestamp=ctx.message.created_at)
        embed.set_image(url=url)
        await ctx.send(embed=embed)

    @commands.command(aliases=['trigger'])
    async def triggered(self, ctx, member: discord.Member = None):
        """Add a triggered filter to a profile picture."""
        user = member or ctx.message.author
        av = str(user.avatar_url_as(format='png'))
        url = f'https://some-random-api.ml/canvas/triggered?avatar={av}'
        embed = discord.Embed(color=0x5643fd, timestamp=ctx.message.created_at)
        embed.set_image(url=url)
        await ctx.send(embed=embed)

    @commands.command()
    async def greyscale(self, ctx, member: discord.Member = None):
        """Add a greyscale filter to a profile picture."""
        user = member or ctx.message.author
        av = str(user.avatar_url_as(format='png'))
        url = f'https://some-random-api.ml/canvas/greyscale?avatar={av}'
        embed = discord.Embed(color=0x5643fd, timestamp=ctx.message.created_at)
        embed.set_image(url=url)
        await ctx.send(embed=embed)

    @commands.command()
    async def invertgreyscale(self, ctx, member: discord.Member = None):
        """Add an inverted and greyscaled filter to a profile picture."""
        user = member or ctx.message.author
        av = str(user.avatar_url_as(format='png'))
        url = f'https://some-random-api.ml/canvas/invertgreyscale?avatar={av}'
        embed = discord.Embed(color=0x5643fd, timestamp=ctx.message.created_at)
        embed.set_image(url=url)
        await ctx.send(embed=embed)

    @commands.command(aliases=['brightness'])
    async def bright(self, ctx, member: discord.Member = None):
        """Add a bright filter to a profile picture."""
        user = member or ctx.message.author
        av = str(user.avatar_url_as(format='png'))
        url = f'https://some-random-api.ml/canvas/brightness?avatar={av}'
        embed = discord.Embed(color=0x5643fd, timestamp=ctx.message.created_at)
        embed.set_image(url=url)
        await ctx.send(embed=embed)

    @commands.command()
    async def sepia(self, ctx, member: discord.Member = None):
        """Add a sepia filter to a profile picture."""
        user = member or ctx.message.author
        av = str(user.avatar_url_as(format='png'))
        url = f'https://some-random-api.ml/canvas/sepia?avatar={av}'
        embed = discord.Embed(color=0x5643fd, timestamp=ctx.message.created_at)
        embed.set_image(url=url)
        await ctx.send(embed=embed)

    @commands.command()
    async def threshold(self, ctx, member: discord.Member = None):
        """Add a black and white filter to a profile picture."""
        user = member or ctx.message.author
        av = str(user.avatar_url_as(format='png'))
        url = f'https://some-random-api.ml/canvas/threshold?avatar={av}'
        embed = discord.Embed(color=0x5643fd, timestamp=ctx.message.created_at)
        embed.set_image(url=url)
        await ctx.send(embed=embed)

    @commands.command()
    async def red(self, ctx, member: discord.Member = None):
        """Add a red filter to a profile picture."""
        user = member or ctx.message.author
        av = str(user.avatar_url_as(format='png'))
        url = f'https://some-random-api.ml/canvas/red?avatar={av}'
        embed = discord.Embed(color=0x5643fd, timestamp=ctx.message.created_at)
        embed.set_image(url=url)
        await ctx.send(embed=embed)

    @commands.command()
    async def green(self, ctx, member: discord.Member = None):
        """Add a green filter to a profile picture."""
        user = member or ctx.message.author
        av = str(user.avatar_url_as(format='png'))
        url = f'https://some-random-api.ml/canvas/green?avatar={av}'
        embed = discord.Embed(color=0x5643fd, timestamp=ctx.message.created_at)
        embed.set_image(url=url)
        await ctx.send(embed=embed)

    @commands.command()
    async def blue(self, ctx, member: discord.Member = None):
        """Add a blue filter to a profile picture."""
        user = member or ctx.message.author
        av = str(user.avatar_url_as(format='png'))
        url = f'https://some-random-api.ml/canvas/blue?avatar={av}'
        embed = discord.Embed(color=0x5643fd, timestamp=ctx.message.created_at)
        embed.set_image(url=url)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Sra(client))