import discord
from discord.ext import commands
from os import environ
from dotenv import load_dotenv
import json
from difflib import get_close_matches
import aiofiles
from typing import Optional


load_dotenv()
TOKEN = environ["TOKEN"]
client = commands.Bot(command_prefix="s!", intents=discord.Intents.all())

@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def ping(ctx):
    await ctx.send(f"🏓 Pong with {str(round(client.latency, 2))}")

# Load the knowledge base from a JSON file
async def loadFile(file_path: str) -> Optional[dict]:
    try:
        async with aiofiles.open(file_path, 'r') as file:
            data = await file.read()
            return json.loads(data)
    except Exception as e:
        print(f"Error loading file: {e}")
        return None
    
# Find the best match for the user's question
def bestMatch(user_question: str, questions: list[str]) -> Optional[str]:
    matches = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

# Get the answer for the matched question
def getAnswer(question: str, knowledge_base: dict) -> Optional[str]:
    for q in knowledge_base["questions"]:
        if q["question"].lower() == question.lower():
            return q["answer"]
    return None

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.channel.id == 1255593067436834817: 
        knowledge_base = await loadFile("depressed.json")
        if not knowledge_base:
            await message.channel.send("Error loading knowledge base.")
            return

        user_input = message.content.lower()
        best_match = bestMatch(user_input, [q["question"].lower() for q in knowledge_base["questions"]])

        if best_match:
            answer = getAnswer(best_match, knowledge_base)
            if answer:
                await message.channel.send(answer)
            else:
                await message.channel.send("I don't know how to respond to that.")
        else:
            await message.channel.send("I don't understand your question.")

    await client.process_commands(message)

client.run(TOKEN)