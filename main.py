import discord
from dotenv import load_dotenv
import os
import random
from time import sleep
import requests

load_dotenv()                                                                                                                                                                                                                            
bot = discord.Bot(intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")


@bot.slash_command()
async def hello(ctx, name: str = None):
    name = name or ctx.author.name
    print('before response ')
    
    await ctx.respond(f"Hello {name}!")
    
    print('after response')

@bot.command()
async def gtn(ctx):
    """A Slash Command to play a Guess-the-Number game."""
    guess = None
    await ctx.respond('Guess a number between 1 and 10.')
    guess = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
    print(guess)
    if int(guess.content) == 5:
          await ctx.send('You guessed it!')
     else:
          await ctx.send('Nope, try again.')
          
@bot.command()


bot.run(os.getenv('TOKEN'))

