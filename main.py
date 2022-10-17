import discord
from dotenv import load_dotenv
import os
from pokiAPI.pokimon import get_details

load_dotenv() #load in env vars


intents = discord.Intents.all()

bot = discord.Bot(intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")


# @bot.slash_command()
# async def hello(ctx, name: str = None):
#     name = name or ctx.author.name
#     await ctx.respond(f"Hello {name}!")
    

## Command that allows you to guess a number
@bot.command()
async def gtn(ctx):
    """A Slash Command to play a Guess-the-Number game."""
    guess = None
    await ctx.respond('Guess a number between 1 and 10.')
    guess = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
    if int(guess.content) == 5:
        await ctx.send('You guessed it!')
    else:
        await ctx.send('Nope, try again.')

    
@bot.command(name = 'test',description = 'This gives a pokemons attributes')
async def get_pokemon(ctx, pokemon: str,):
    await ctx.respond('Name a pokemon')
    await ctx.respond('Enter preferred details')
    items = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
    await ctx.respond(get_details(pokemon, items.content))
@bot.command()
async def test_function(ctx, name: str):
    await ctx.respond('this function works')

bot.run(os.getenv('TOKEN'))

