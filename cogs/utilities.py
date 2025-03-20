import discord
from discord.ext import commands
import random

import giphy_client
from giphy_client.rest import ApiException

import wolframalpha
import wikipedia as wp
import googletrans
from googletrans import Translator
import aiohttp
import random
import asyncio
import io

import wikipedia

f = open("assets/topic.txt", "r")
topics = f.readlines()

def wiki_summary(arg):
    definition = wp.summary(arg, sentences=3, chars=1000,auto_suggest=True, redirect=True)
    return definition

class Utilities(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['av', 'pfp'])
    async def avatar(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        embed = discord.Embed(title=f"Avatar for {member.name}",
        description=f"**Link as**\n[png]({member.avatar_url_as(format='png', size=1024)}) | [jpg]({member.avatar_url_as(format='jpg', size=1024)}) | [webp]({member.avatar_url_as(format='webp', size=1024)})", 
        colour=discord.Color.blue())
        embed.set_image(url=member.avatar_url)
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"requested by {ctx.author.name}")
        await ctx.send(embed=embed)

    @commands.command()
    async def topic(self, ctx):
        random_topic = random.choice(topics)
        embed = discord.Embed(title=random_topic, color=discord.Colour.blue())
        embed.set_footer(icon_url=ctx.author.avatar_url,
                        text=f"requested by {ctx.author.name}")

        await ctx.send(embed=embed)


    #choose-----------------------------------------------------
    @commands.command()
    async def choose(self, ctx, *, choice):
        choice1, choice2 = choice.split(",")
        choose = [choice1, choice2]
        res = random.choice(choose)
        await ctx.send(f"I choose `{res}`")

    @commands.command(aliases=["Q"])
    async def q(self, ctx, *,msg):
        question = msg
        app_id = '8UKEXP-5V4PL4QYQ7'
        client = wolframalpha.Client(app_id)
        res = client.query(question)
        answer = next(res.results).text

        await ctx.send(answer)

    @commands.command(aliases=['pl'])
    async def poll(self,ctx, *, msg):
        embed = discord.Embed(title="📊 poll", description=f"**{msg}**")

        msg = await ctx.send(embed=embed)

        await msg.add_reaction("✅")
        await msg.add_reaction("❎")
        await ctx.message.delete()

    @commands.command(aliases=["tr"])
    async def translate(self, ctx,lang_to, *args):

        lang_to = lang_to.lower()
        if lang_to not in googletrans.LANGUAGES and lang_to not in googletrans.LANGCODES:
            embed = discord.Embed(title="Error",description="Invalid Language")
            await ctx.send(embed=embed)
        text = ' '.join(args)

        translator = Translator()
        text_translated = translator.translate(text, dest=lang_to).text

        embed = discord.Embed(title ="Translator" ,description = text_translated,color=discord.Colour.blue())
        embed.set_footer(icon_url="https://upload.wikimedia.org/wikipedia/commons/d/db/Google_Translate_Icon.png",text="powered by Google Translate")
        await ctx.send(embed=embed)

    #giphy-------------------------------------------------------

    @commands.command()
    async def gif(self, ctx,*,q="anime"):

        api_key="FLOCKkbSb9br9Q3mlOyAJAZuy212D8ld"
        api_instance = giphy_client.DefaultApi()

        try:
        # Search Endpoint

            api_response = api_instance.gifs_search_get(api_key, q, limit=5, rating='pg13')
            lst = list(api_response.data)
            giff = random.choice(lst)

            emb = discord.Embed(title=q)
            emb.set_image(url = f'https://media.giphy.com/media/{giff.id}/giphy.gif')
            emb.set_footer(icon_url="https://giphy.com/static/img/giphy_logo_square_social.png",text=f"from giphy")


            await ctx.channel.send(embed=emb)
        except ApiException as e:
            print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)

    #wiki===================================================================================

    @commands.command(aliases=["wikipedia","Wiki"])
    async def wiki(self, ctx,*,question):
        page = wp.page({question})
        em = discord.Embed(title= page.title , description = wiki_summary(question), )
        em.set_image(url= page.images[0])
        em.set_footer(icon_url="https://cdn.freebiesupply.com/images/large/2x/wikipedia-logo-transparent.png",text=f"from wikipedia")

        await ctx.send(embed=em)

    @commands.command(aliases=["em"])
    async def embed_say(slef, ctx, *, message):
        embed = discord.Embed(description=f"{message}", colour=discord.Colour.blue())
        embed.set_footer(icon_url=ctx.author.avatar_url,text=f"requested by {ctx.author.name}")

        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(aliases=["em2"])
    async def embed_say2(self, ctx, *, message):
        embed = discord.Embed(description=f"{message}", colour=discord.Colour.blue())

        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command()
    async def say(self, ctx,*,message):
        await ctx.send(message)



def setup(client):
    client.add_cog(Utilities(client))