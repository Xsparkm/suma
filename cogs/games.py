import discord
from discord.ext import commands

import akinator as ak
import random
from random import randint


class Games(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command()
    async def aki(self, ctx,name='id'):
        await ctx.send("Akinator is here to guess!")

        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower(
            ) in ["y", "n", "p", "b"]

        try:
            aki = ak.Akinator()
            q = aki.start_game()
            while aki.progression <= 80:
                await ctx.send(q)
                await ctx.send("Your answer:(y/n/p/b)")
                msg = await self.client.wait_for("message", check=check)
                if msg.content.lower() == "b":
                    try:
                        q = aki.back()
                    except ak.CantGoBackAnyFurther:
                        await ctx.send(e)
                        continue
                else:
                    try:
                        q = aki.answer(msg.content.lower())
                    except ak.InvalidAnswerError as e:
                        await ctx.send(e)
                        continue
            aki.win()
            embed = discord.Embed(color=ctx.author.top_role.colour)
            embed.add_field(name=f"It's {aki.first_guess['name']}", value = aki.first_guess['description'])
            embed.set_image(url=aki.first_guess['absolute_picture_path'])
            embed.set_footer(text="Is it correct?(y/n)")

            await ctx.send(embed=embed)

            correct = await self.client.wait_for("message", check=check)
            if correct.content.lower() == "y":
                await ctx.send("Yay\n")
            else:
                await ctx.send("GG you won!!\n")
        except Exception as e:
            await ctx.send(e)


    @commands.command()
    async def guess(self, ctx):

        await ctx.send(f"Hello {ctx.author.name}! I'm thinking of a number between 1 and 50. You are given 5 tries to find the number. Good luck!")
        secretNumber = random.randint(1,50)

        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel  and message.content.isdigit()

        for guessesTaken in range(5):

            guess = int((await self.client.wait_for('message', check=check)).content)

            if guess < secretNumber:
                await ctx.send("Your guess is too low")
            elif guess > secretNumber:
                await ctx.send("Your guess is too high")
            else:
                await ctx.send(f"GG! You correctly guessed the number in {guessesTaken + 1} guesses!")

        else:
            await ctx.send(f"Nope, sorry, you took too many guesses. The number I was thinking of was **{secretNumber}**")

    @commands.command(aliases=['slots', 'bet'])
    async def slot(self,ctx):
        """ Roll the slot machine """
        emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
        a = random.choice(emojis)
        b = random.choice(emojis)
        c = random.choice(emojis)

        slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"

        if (a == b == c):
            await ctx.send(f"{slotmachine} All matching, you won! <a:lil_swag:828986742836822057:")
        elif (a == b) or (a == c) or (b == c):
            await ctx.send(f"{slotmachine} 2 in a row ! <a:ultra_yay:828986892002263061> ")
        else:
            await ctx.send(f"{slotmachine} No match, you lost, ||noob <a:kek:828987935084773396:>")

    @commands.command(aliases=['flip', 'coin'])
    async def coinflip(self, ctx):
        coinsides = ['Heads', 'Tails']
        await ctx.send(
            f"**{ctx.author.name}** flipped a coin and got **{random.choice(coinsides)}**!")


def setup(client):
    client.add_cog(Games(client))