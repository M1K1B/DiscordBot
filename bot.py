'''
    !roastme bot
    This bot will roast you on command
'''

#!roastme-voice

import os
import random

import discord
from dotenv import load_dotenv

import secrets

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
SERVER = os.getenv('DISCORD_SERVER')

roasts = [
    'Your hair line is deeper than ocean.',
    'Your forhead is so big, i can park a car on it.',
    'You are the biggest roast possible.',
    'Your mom said you were the biggest mistake she made.',
    'You know.. ugly begins with U.',
    'If you type one more message, I am going to kill you.'
]

roastsRs = [
    'Tvoj autfit mi se bas svidja, sklopio si boje kao daltonista.',
    'Znas.. sto vise gladam u tebe, sve vise hocu da se ubijem.',
    'Koliki ti je nos, da ne umes da pricas mislio bi da si slon.',
    'Ako napises jos jednu poruku ubicu te, majke mi.'
]

roastsCs = [
    'Decoy is more usefull than you.',
    'You are as usefull as right CTRL.',
    'I would rather play with a bot then with you.',
    'If i need one more player for full queue and you were the last player on the Earth, I would play 4v5',
    "You are so fat thet smoke does't cover you."
]

roastsCsRs = [
    'Koristan si kao desni CTRL.',
    'Dikoi je korisniji od tebe.',
    'Pre bi igrao sa botom nego sa tobom.',
    'Toliko si debeo da se vidis kroz smoke.'
]

botHelp = 'Commands for bot on English:\n\
    !roastme ........ Bot will roast you on English\n\
    !roastme-cs ..... Bot will roast you about CS:GO\n\
Komande za bota na srpskom:\n\
    !roastme-rs ..... Bot ce da te roustuje na srpskom\n\
    !roastme-cs-rs .. Bot ce da te roustuje za CS:GO'

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content == '!roastme':
        roast = random.choice(roasts)
        await message.channel.send(roast)
    elif message.content == '!roastme-rs':
        roast = random.choice(roastsRs)
        await message.channel.send(roast)
    elif message.content == '!roastme-cs':
        roast = random.choice(roastsCs)
        await message.channel.send(roast)
    elif message.content == '!roastme-cs-rs':
        roast = random.choice(roastsCsRs)
        await message.channel.send(roast)
    elif message.content == '!roastme-help':
        await message.channel.send(botHelp)

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == SERVER:
            break
    
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    for member in guild.members:
        print(member.name)

client.run(TOKEN)