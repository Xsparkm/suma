from os import name
import discord
from discord.ext import commands
from discord.ext.commands.core import command

class Info(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["userinfo", "aboutuser"])
    async def user(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        roles = [role for role in member.roles]
        embed = discord.Embed(colour=member.colour,
                            timestamp=ctx.message.created_at)
        embed.set_author(name=f"User info - {member}")
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"Requested by {ctx.author}",
                        icon_url=ctx.author.avatar_url)
        embed.add_field(name="ID: ", value=member.id,  )
        embed.add_field(
            name="Created account at: ",
            value=member.created_at.strftime("%a, %d %#B %Y, %I:%M %p UTC"))
        embed.add_field(
            name="Joined server at: ",
            value=member.joined_at.strftime("%a, %d %#B %Y, %I:%M %p UTC"))
        embed.add_field(name=f"Roles ({len(roles)})",
                        value=" ".join([role.mention for role in roles]),
                         )
        embed.add_field(name="Top role:",
                        value=member.top_role.mention,
                         )
        embed.add_field(name="Bot? ", value=member.bot,  )
        embed.add_field(name="Activity", value=f"{member.activity}", inline=False)
        if member.status == discord.Status.online:
            embed.add_field(name="Status:", value='online',  )
        elif member.status == discord.Status.dnd:
            embed.add_field(name="Status:", value='dnd',  )
        elif member.status == discord.Status.offline:
            embed.add_field(name="Status:", value='invisible',  )
        elif member.status == discord.Status.idle:
            embed.add_field(name="Status:", value='idle')
        await ctx.send(embed=embed)

    #################################################
    #help############################################
    #################################################

    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        em = discord.Embed(title='ℹ️ Help',description=" ",color=ctx.author.color)

        em.add_field(name="📦 Utilities", value="avatar, userinfo, wiki, gif, q, poll, translate",
        inline=False)
        em.add_field(name="🌸 Anime" ,value="anime, mal",
        inline=False)
        em.add_field(name="📸 Images", value="glass, gay, invert, wasted, triggered, greyscale, invertgreyscale, bright, sepia, treshold, red, green, blue ",
        inline=False)
        em.add_field(name="🔮 Fun" ,value="rickroll, space, howgay, treat, choose, fortune, topic, pokemon",
        inline=False)
        em.add_field(name="🦄 Animals",value=" cat, dog, panda, koala, fox, bird",
        inline=False)
        em.add_field(name="🎲 Games",value="aki, guess, slot",
        inline=False)
        em.add_field(name="🏵 Roleplay", value="hug, pat, wink",
        inline=False)
        em.set_footer(icon_url=ctx.author.avatar_url, text=f"requested by {ctx.author.name}")

        await ctx.send(embed=em)



def setup(client):
    client.add_cog(Info(client))