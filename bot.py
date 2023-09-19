# You'll need a .py key for the bot.
import key
import discord
import logging
import requests
from discord.ext import commands

logger = logging.getLogger('discord')
logging.basicConfig(level=logging.INFO)

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='.', intents=intents)

@bot.command()
async def ambatu(msg):
    await msg.channel.send('https://www.youtube.com/watch?v=9ifE7MvC7ng') 

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    await bot.process_commands(message) 
    if message[0] == '.':
        return
    if message.author == bot.user:
        return
    if message.content.startswith('$blow'):
        await message.channel.send('Im bout to BLOWWW!')

bot.run(key.token)

