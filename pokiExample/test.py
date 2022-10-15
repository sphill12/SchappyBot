import requests
import json


BASE_URL = "https://pokeapi.co/api/v2/pokemon/"


# response = requests.get(BASE_URL + 'ditto')

# data = json.loads(response.text)
# print(data)

# poki_items = []

# for key in data.keys():
#   print(key)
#   poki_items.append(key)


def get_details(pokemon: str, description: str | list) -> str | list:
    # request the page containing information on the pokemon
    url = BASE_URL + pokemon.lower()
    response = requests.get(url)
    data = json.loads(response.text)
    if type(description) == list:
        for i in description:
            print(data[i])
    else:
        print(data[description])


##Discord slash command to grab all data from pokedex

# @bot.slash_command()
# async def hello(ctx, name: str = None):
#     name = name or ctx.author.name
#     await ctx.respond(f"Hello {name}!")


# ## Command that allows you to guess a number
# @bot.command()
# async def gtn(ctx):
#     """A Slash Command to play a Guess-the-Number game."""
#     guess = None
#     await ctx.respond('Guess a number between 1 and 10.')
#     guess = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
#     if int(guess.content) == 5:
#         await ctx.send('You guessed it!')
#     else:
#         await ctx.send('Nope, try again.')
