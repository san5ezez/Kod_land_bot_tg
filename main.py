import discord
from discord.ext import commands
from discord import *
import asyncio
import requests
import os
import random
img = os.listdir('images')

token =  "token"
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.command()
async def mem(ctx):
    random_file = random.choice(img)
    with open(f'images/{random_file}', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)


def get_sobaka_image_url():    
    url1 = 'https://random.dog/woof.json' 
    res = requests.get(url1)
    data = res.json()
    print(data)
    return data['url']


@bot.command('sobaka')
async def duck(ctx):
    '''По команде duck вызывает функцию get_duck_image_url'''
    image_url = get_sobaka_image_url()
    await ctx.send(image_url)



def get_lisa_image_url():    
    url = 'https://randomfox.ca/floof/'
    res = requests.get(url)
    data = res.json()
    return data['image']

@bot.command(name='lisa')
async def lisa(ctx):
    image_url = get_lisa_image_url()
    await ctx.send(image_url)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def rick_astly(ctx):
    await ctx.send('https://tenor.com/view/rickroll-meme-internet-never-gonna-gif-26474110')

@bot.command(name="timer")
async def timer(ctx, number):
    number = int(number)
    message = await ctx.send(number)
    while number != 0:
        number -= 1
        await message.edit(content=number)
        await asyncio.sleep(1)
    await message.edit(content='Ended!')

bot.run(token)