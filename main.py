import discord
from discord.ext import commands
client = commands.Bot(command_prefix=">")

import random
import asyncio
import time
import pyfiglet
import aiohttp
import requests
import akinator as ak
import os

warn_channel = 814179067934408766
client.remove_command("help")

f = open("topic.txt", "r")
topics = f.readlines()

f = open("hi.txt", "r")
wavegifs = f.readlines()

f = open("fortune.txt", "r")
fortune_reply = f.readlines()
#setup==================================================


@client.event
async def on_ready():
	print("bot is ready")


async def ch_pr():
	await client.wait_until_ready()

	statuses = ["with you", ">help", "in Isle", "V 1.0"]

	while not client.is_closed():

		status = random.choice(statuses)
		await client.change_presence(activity=discord.Game(name=status))

		await asyncio.sleep(30)


client.loop.create_task(ch_pr())

#events==========


filtered_words = ["<@636055755413389322>","<@758922777176178718>"]

@client.event
async def on_message(msg):
	if ":" == msg.content[0] and ":" == msg.content[-1]:
		emoji_name = msg.content[1:-1]
		for emoji in msg.guild.emojis:
			if emoji_name == emoji.name:
				await msg.channel.send(str(emoji))
				await msg.delete()
				break

	await client.process_commands(msg)


#avatar-----------------------------------------------------------------


@client.command(aliases=['av', 'pfp'])
async def avatar(ctx, member: discord.Member):
	embed = discord.Embed(description=member.mention,
	                      colour=discord.Colour.blue())
	embed.set_image(url=member.avatar_url)
	embed.set_footer(icon_url=ctx.author.avatar_url,
	                 text=f"requested by {ctx.author.name}")

	await ctx.send(embed=embed)


#reactions---------------------------------

#kill

killgifs = [
    'https://i.imgur.com/7et8lYx.gif',
    'https://i.imgur.com/Y9FsSXa.gif',
    'https://i.imgur.com/Tra6zBW.gif',
]


@client.command()
async def kill(ctx, member: discord.Member):
	embed = discord.Embed(title=ctx.author.name + " killed " + member.name,
	                      colour=discord.Colour.red())

	random_link = random.choice(killgifs)
	embed.set_image(url=random_link)

	await ctx.send(embed=embed)


@client.command()
async def wave(ctx):
	embed = discord.Embed(title="Hello!", color=discord.Colour.blue())

	random_wave = random.choice(wavegifs)
	embed.set_image(url=random_wave)

	await ctx.send(embed=embed)


#hug

huggifs = []


@client.command()
async def hug(ctx, member: discord.Member):
	embed = discord.Embed(title=ctx.author.name + " hugs " + member.name,
	                      colour=discord.Colour.pink())

	random_link = random.choice(huggifs)
	embed.set_image(url=random_link)

	await ctx.send(embed=embed)


#fortune---------------------------------------------------------------------


@client.command(aliases=['8ball'])
async def fortune(ctx, *, msg):
	embed = discord.Embed(title="🎱fortune", colour=discord.Colour.blue())

	random_message = random.choice(fortune_reply)
	embed.add_field(name=ctx.author.name + " is asking: ", value=f"{msg}")
	embed.add_field(name=" <a:NezukoVibing:792755439988113479> my answer is: ",
	                value=random_message)

	await ctx.send(embed=embed)


#topic----------------------------------------------------------------------------


@client.command()
async def topic(ctx):
	random_topic = random.choice(topics)
	embed = discord.Embed(title=random_topic, color=discord.Colour.blue())
	embed.set_footer(icon_url=ctx.author.avatar_url,
	                 text=f"requested by {ctx.author.name}")

	await ctx.send(embed=embed)


#choose-----------------------------------------------------
@client.command()
async def choose(ctx, *, choice):
	choice1, choice2 = choice.split(",")
	choose = [choice1, choice2]
	res = random.choice(choose)
	await ctx.send(f"I choose `{res}`")


#coinflip-------------------------------------------------------


@client.command(aliases=['flip', 'coin'])
async def coinflip(ctx):
	coinsides = ['Heads', 'Tails']
	await ctx.send(
	    f"**{ctx.author.name}** flipped a coin and got **{random.choice(coinsides)}**!")


#slot


@client.command(aliases=['slots', 'bet'])
async def slot(ctx):
	""" Roll the slot machine """
	emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
	a = random.choice(emojis)
	b = random.choice(emojis)
	c = random.choice(emojis)

	slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"

	if (a == b == c):
		await ctx.send(f"{slotmachine} All matching, you won! 🎉")
	elif (a == b) or (a == c) or (b == c):
		await ctx.send(f"{slotmachine} 2 in a row, not bad! 🎉")
	else:
		await ctx.send(f"{slotmachine} No match, you lost 😢")


#space===========================================
@client.command(pass_context=True)
async def space(ctx, *, msg):
	"""Add n spaces between each letter. Ex: [p]space 2 thicc"""
	await ctx.message.delete()
	if msg.split(' ', 1)[0].isdigit():
		spaces = int(msg.split(' ', 1)[0]) * ' '
		msg = msg.split(' ', 1)[1].strip()
	else:
		spaces = ' '
	spaced_message = spaces.join(list(msg))
	await ctx.send(spaced_message)


#whois=====================================================================


@client.command(aliases=["userinfo", "aboutuser"])
async def user(ctx, member: discord.Member = None):
	member = ctx.author if not member else member
	roles = [role for role in member.roles]
	embed = discord.Embed(colour=member.colour,
	                      timestamp=ctx.message.created_at)
	embed.set_author(name=f"User info - {member}")
	embed.set_thumbnail(url=member.avatar_url)
	embed.set_footer(text=f"Requested by {ctx.author}",
	                 icon_url=ctx.author.avatar_url)
	embed.add_field(name="ID: ", value=member.id, inline=True)
	embed.add_field(
	    name="Created account at: ",
	    value=member.created_at.strftime("%a, %d %#B %Y, %I:%M %p UTC"))
	embed.add_field(
	    name="Joined server at: ",
	    value=member.joined_at.strftime("%a, %d %#B %Y, %I:%M %p UTC"))
	embed.add_field(name=f"Roles ({len(roles)})",
	                value=" ".join([role.mention for role in roles]),
	                inline=True)
	embed.add_field(name="Top role:",
	                value=member.top_role.mention,
	                inline=True)
	embed.add_field(name="Bot? ", value=member.bot, inline=True)
	embed.add_field(name="Activity", value=f"{member.activity}", inline=False)
	if member.status == discord.Status.online:
		embed.add_field(name="Status:", value='online', inline=True)
	elif member.status == discord.Status.dnd:
		embed.add_field(name="Status:", value='dnd', inline=True)
	elif member.status == discord.Status.offline:
		embed.add_field(name="Status:", value='invisible', inline=True)
	elif member.status == discord.Status.idle:
		embed.add_field(name="Status:", value='idle')
	await ctx.send(embed=embed)


#treat===========================================================


@client.command(case_insensitive=True)
async def treat(ctx, member: discord.Member):
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
		reaction, user = await client.wait_for('reaction_add',
		                                       timeout=timeout,
		                                       check=check)

	except asyncio.TimeoutError:
		msg = (f"{member.mention} didn't accept the treat in time!!")
		await ctx.channel.send(msg)

	else:
		await ctx.channel.send(
		    f"{member.mention} You have accepted {ctx.author.name} is offer!")


#ascii


@client.command()
async def ascii(ctx, *, text=None):
	if text is None:
		await ctx.send("You must input some text to make into Ascii!")
		return
	result = pyfiglet.figlet_format(text)

	embed = discord.Embed(description=f"{result}")
	await ctx.send(embed=embed)


#howgay
@client.command(aliases=['HOWGAY', 'Howgay'])
async def howgay(ctx, member: discord.Member = None):
	if not member:
		member = ctx.author

	gaycount = random.randint(0, 100)
	embed = discord.Embed(
	    title=f"Let is see how gay {member.name} is. :rainbow_flag:",
	    description=f"{gaycount}%",
	    color=discord.Color(0xff55ff))
	await ctx.send(embed=embed)


#rickroll=================================================================


@client.command()
async def rickroll(ctx, time: int):
	if time > 1000:
		await ctx.send("I can't wait that long-")
		return
	one = await ctx.send(f"Rickrolling you in {time}")
	for i in range(time):
		time -= 1
		await asyncio.sleep(1)
		await one.edit(content=f"Rickrolling you in {time}")
	await one.edit(
	    content=
	    "https://tenor.com/view/rick-astley-rick-roll-dancing-dance-moves-gif-14097983"
	)


#anime==================================================


@client.command()
async def anime(ctx, *, animeName: str):

	api = 'https://graphql.anilist.co'
	query = '''
    query ($name: String){
      Media(search: $name, type: ANIME) {
        id
        idMal
        description
        title {
          romaji
          english
        }
        coverImage {
          large
        }
        startDate {
          year
          month
          day
        }
        endDate {
          year
          month
          day
        }
        synonyms
        format
        status
        episodes
        duration
        nextAiringEpisode {
          episode
        }
        averageScore
        meanScore
        source
        genres
        tags {
          name
        }
        studios(isMain: true) {
          nodes {
            name
          }
        }
        siteUrl
      }
    }
    '''
	variables = {'name': animeName}

	async with aiohttp.ClientSession() as session:
		async with session.post(api,
		                        json={
		                            'query': query,
		                            'variables': variables
		                        }) as r:
			if r.status == 200:
				json = await r.json()
				data = json['data']['Media']

				embed = discord.Embed(color=ctx.author.top_role.colour)
				embed.set_footer(
				    text='API provided by AniList.co | ID: {}'.format(
				        str(data['id'])))
				embed.set_thumbnail(url=data['coverImage']['large'])
				if data['title']['english'] == None or data['title'][
				    'english'] == data['title']['romaji']:
					embed.add_field(name='Title',
					                value=data['title']['romaji'],
					                inline=False)
				else:
					embed.add_field(name='Title',
					                value='{} ({})'.format(
					                    data['title']['english'],
					                    data['title']['romaji']),
					                inline=False)

				#embed.add_field(name='Beschreibung', value=data['description'], inline=False)
				if data['synonyms'] != []:
					embed.add_field(name='Synonyme',
					                value=', '.join(data['synonyms']),
					                inline=True)

				embed.add_field(name='Type',
				                value=data['format'].replace(
				                    '_', ' ').title().replace('Tv', 'TV'),
				                inline=True)
				if data['episodes'] > 1:
					embed.add_field(name='Episodes',
					                value='{} hrs {} min'.format(
					                    data['episodes'], data['duration']),
					                inline=True)
				else:
					embed.add_field(name='Duration',
					                value=str(data['duration']) + ' min',
					                inline=True)

				embed.add_field(name='Start date',
				                value='{}.{}.{}'.format(
				                    data['startDate']['day'],
				                    data['startDate']['month'],
				                    data['startDate']['year']),
				                inline=True)
				if data['endDate']['day'] == None:
					embed.add_field(
					    name='Released Folgen',
					    value=data['nextAiringEpisode']['episode'] - 1,
					    inline=True)
				elif data['episodes'] > 1:
					embed.add_field(name='End date',
					                value='{}.{}.{}'.format(
					                    data['endDate']['day'],
					                    data['endDate']['month'],
					                    data['endDate']['year']),
					                inline=True)

				embed.add_field(name='Status',
				                value=data['status'].replace('_', ' ').title(),
				                inline=True)

				try:
					embed.add_field(name='Haupt-Studio',
					                value=data['studios']['nodes'][0]['name'],
					                inline=True)
				except IndexError:
					pass
				embed.add_field(name='Score',
				                value=data['averageScore'],
				                inline=True)
				embed.add_field(name='Genres',
				                value=', '.join(data['genres']),
				                inline=False)
				tags = ''
				for tag in data['tags']:
					tags += tag['name'] + ', '
				embed.add_field(name='Tags', value=tags[:-2], inline=False)
				try:
					embed.add_field(name='Adapted from',
					                value=data['source'].replace('_',
					                                             ' ').title(),
					                inline=True)
				except AttributeError:
					pass

				embed.add_field(name='AniList Link',
				                value=data['siteUrl'],
				                inline=False)
				embed.add_field(name='MyAnimeList Link',
				                value='https://myanimelist.net/anime/' +
				                str(data['idMal']),
				                inline=False)
				await ctx.send(embed=embed)

			else:
				await ctx.send(':x: Unable find a suitable anime!')


#text-covert=========================================================


@client.command()
async def convert(ctx, *, msg):

	url = "https://ajith-fancy-text-v1.p.rapidapi.com/text"

	querystring = {"text": {msg}}

	headers = {
	    'x-rapidapi-key': "6f4a1d9629msh23ff15a3e3354d7p112b30jsn67c80acd40d2",
	    'x-rapidapi-host': "ajith-Fancy-text-v1.p.rapidapi.com"
	}

	response = requests.request("GET",
	                            url,
	                            headers=headers,
	                            params=querystring)

	await ctx.send(message)




#aki#######################


@client.command(aliases=["aki"])
async def akinator(ctx):
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
			msg = await client.wait_for("message", check=check)
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
		embed.add_field(title=f"It's {aki.first_guess['name']}", description = ({aki.first_guess['description']}))
		embed.set_image(url=aki.first_guess['absolute_picture_path'])
		embed.set_footer(text="Is it correct?(y/n)")

		await ctx.send(embed=embed)

		correct = await client.wait_for("message", check=check)
		if correct.content.lower() == "y":
			await ctx.send("Yay\n")
		else:
			await ctx.send("GG you won!!\n")
	except Exception as e:
		await ctx.send(e)

#################################################
#ping############################################
#################################################


################################################
#help############################################
#################################################

@client.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(title='ℹ️ Help',description="Use r!help <command> for more details of a command.",color=ctx.author.color)

    em.add_field(name="Roleplay", value="kill, hi, hug")
    em.add_field(name="Utilities", value="avatar, anime, userinfo")
    em.add_field(name="Fun" ,value="rickroll, space, howgay, treat, choose, fortune, topic")
    em.add_field(name="Games", value="slot, coinflip, akinator")

    await ctx.send(embed=em)

#run#####################################################################

client.run(os.environ['token'])
