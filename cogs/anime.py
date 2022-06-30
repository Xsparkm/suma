from os import name
from aiohttp import client_reqrep
from animec import anicore
import discord
from discord.ext import commands
import aiohttp
import animec
from animec import aninews
from discord.ext.commands.core import command
from jikanpy import Jikan
myanimelist = Jikan()


class Anime(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command()
    async def mal(self, ctx,name='id'):

        data = myanimelist.user(username=name)
        data.get('image_url')

        embed = discord.Embed(title=f'Set MyAnimeList Profile `{data.get("username")}`',color= discord.Colour.blue())
        embed.set_author(name='MAL | myanimelist.net')

        
        embed.set_thumbnail(url=data.get('image_url'))

        embed.add_field(
            name='Anime Stats',  
            value=f'Days Watched: {data.get("anime_stats")["days_watched"]}\n'
                    f'Mean Score: {data.get("anime_stats")["mean_score"]}\n'
                    f'Total Entries: {data.get("anime_stats")["total_entries"]}')
        embed.add_field(
            name='Manga Stats',  
            value=f'Days Read: {data.get("manga_stats")["days_read"]}\n'
                    f'Mean Score: {data.get("manga_stats")["mean_score"]}\n'
                    f'Total Entries: {data.get("manga_stats")["total_entries"]}')

        embed.set_footer(text=f'Provided by myanimelist.net')

        await ctx.send(embed=embed)


    @commands.command()
    async def charecter(self,ctx,*,charecter: str):

        char = charsearch(charecter)
        
        em = discord.Embed(title= char.title)
        em.set_image(url= char.image_url)

        await ctx.send(embed= em)

    @commands.command()
    async def animenews(self,ctx):

        news = aninews.Aninews

        em = discord.Embed(title= "", description= "")
        em.add_field(name=news.titles,value=news.description)
        em.set_image(url= news.images)

        await ctx.send(embed = em)

    @commands.command()
    async def anime(self, ctx,*,name):
        r = anicore.Anime(name)
        em = discord.Embed(title= r.name,description=r.description)
        em.add_field(name="Status",value=r.status)
        em.add_field(name="Genres",value=r.genres)        
        em.add_field(name="Episodes",value=r.episodes)
        em.add_field(name="Rating",value=r.rating)
        em.add_field(name="Ranking",value=r.ranked)
        em.add_field(name="Popularity",value=r.popularity)
        em.add_field(name="Favorites",value=r.favorites)
        em.add_field(name="Type",value=r.type)
        em.add_field(name="Producer",value=r.producers)
        em.set_thumbnail(url=r.poster)
        await ctx.send(embed =em)


def setup(client):
    client.add_cog(Anime(client))
