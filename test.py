import asyncio
from btc import getbitcoin
import os
import pprint
import discord
from decouple import config
from discord.ext import commands
import asyncio, random, json
import requests
import discord.utils
from requests import Request, Session


client = commands.Bot(command_prefix = '!')
#load cogs
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'Loaded {extension} category!')

#unload cogs
@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'Unloaded {extension} category!')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


#On ready event to set status
@client.event
async def on_ready():
    print('ready!')
    print(f'{client.user} is online!')
    print(f"With the ID {client.user.id}")



@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("`I was unable to find this command!`")
async def presence():
    await client.wait_until_ready()
    while not client.is_closed():  
        await client.change_presence(activity=discord.Game(name=getbitcoin()))
        await asyncio.sleep(5)
  

@client.command()
async def BTC(ctx):
    await ctx.send(getbitcoin())
    #await ctx.send(pprint.pprint(json.loads(response.text)['data']['1']['quote']['USD']['price']))

#Fetching environment variables
DISCORD_TOKEN = config('DISCORD_TOKEN') 


client.loop.create_task(presence())
#Run bot with token from environment variables
client.run(DISCORD_TOKEN)