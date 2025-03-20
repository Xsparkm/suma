import discord
from discord.ext import commands

import random
import asyncio
import time

f = open("assets/fortune.txt", "r")
fortune_reply = f.readlines()

class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(aliases=['8ball'])
    async def fortune(self,ctx, *, msg):
        embed = discord.Embed(title="🎱fortune", colour=discord.Colour.blue())

        random_message = random.choice(fortune_reply)
        embed.add_field(name=ctx.author.name + " is asking: ", value=f"{msg}")
        embed.add_field(name="my answer is: ",value=random_message)

        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def space(self, ctx, *, msg):
        """Add n spaces between each letter. Ex: [p]space 2 thicc"""
        await ctx.message.delete()
        if msg.split(' ', 1)[0].isdigit():
            spaces = int(msg.split(' ', 1)[0]) * ' '
            msg = msg.split(' ', 1)[1].strip()
        else:
            spaces = ' '
        spaced_message = spaces.join(list(msg))
        await ctx.send(spaced_message)

    @commands.command(case_insensitive=True)
    async def treat(self,ctx, member: discord.Member):
        if member == ctx.author:
            await ctx.send("You can't treat youself!")
            return
        embed = discord.Embed(
            description=
            f'You offered {member.name} a treat! {member.mention} react to the emoji below to accept!',
            color=0x006400)
        timeout = int(15.0)
        message = await ctx.channel.send(embed=embed)

        await message.add_reaction('🍫')

        def check(reaction, user):
            return user == member and str(reaction.emoji) == '🍫'

        try:
            reaction, user = await self.client.wait_for('reaction_add',
                                                timeout=timeout,
                                                check=check)

        except asyncio.TimeoutError:
            msg = (f"{member.mention} didn't accept the treat in time!!")
            await ctx.channel.send(msg)

        else:
            await ctx.channel.send(
                f"{member.mention} You have accepted {ctx.author.name} is offer!")


    @commands.command(aliases=['HOWGAY', 'Howgay'])
    async def howgay(self,ctx, member: discord.Member = None):
        if not member:
            member = ctx.author

        gaycount = random.randint(0, 100)
        embed = discord.Embed(
            title=f"Let is see how gay {member.name} is. :rainbow_flag:",
            description=f"{gaycount}%",
            color=discord.Color(0xff55ff))
        await ctx.send(embed=embed)


    @commands.command()
    async def rickroll(self,ctx, time: int):
        if time > 1000:
            await ctx.send("I can't wait that long-")
            return
        one = await ctx.send(f"Rickrolling you in {time}")
        for i in range(time):
            time -= 1
            await asyncio.sleep(1)
            await one.edit(content=f"Rickrolling you in {time}")
        await one.edit(content="https://tenor.com/view/rick-astley-rick-roll-dancing-dance-moves-gif-14097983")





def setup(client):
    client.add_cog(Fun(client))
