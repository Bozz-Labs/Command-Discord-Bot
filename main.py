import discord
import random
from keep_alive import keep_alive
import os
from discord.utils import get

dnd_mode = True

bot_token = os.environ['bot token']

mean_things = [
    'Ur stupid', 'idiot', 'u look like shrek', 'ima render dummy.html',
    'yur mom', 'PUT SOME CLOTHES ON!!!', 'your homework is EASY lol',
    'I could do this forever!'
]

nice_things = [
    'You are cool!', 'You can do it!', 'I believe in you!',
    'I ran out of nice things to say.'
]

hello = ['Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'hey baby']

client = discord.Client()

bad_words = [
    'shit', 'Shit', 'SHIT', 'fuck', 'Fuck', 'FUCK', 'bitch', 'Bitch', 'BITCH',
    'nigger', 'Nigger', 'NIGGER'
]


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = message.content

    if msg == '<ping>':
        while True:
            await message.author.send('ping')
    if get(message.author.roles,
           name="Server Operator") and msg == '<infinity>':
        num = 1
        while True:
            await message.channel.send(num)
            num += 1
    if msg == 'hello':
        await message.reply(random.choice(hello))
    if msg.startswith('guess what') or msg.startswith(
            'Guess What') or msg.startswith('Guess what') or msg.startswith(
                'guess What') or msg.startswith('GUESS WHAT'):
        await message.channel.send('chicken butt')
        await message.author.send('chicken butt')
    if msg == '<user>':
        await message.channel.send('user: {0.user}'.format(client))
    if msg == '<status>':
        await message.channel.send('online, in development')
    if msg == '<mean>':
        await message.channel.send(random.choice(mean_things))
    if msg == '<nice>':
        await message.channel.send(random.choice(nice_things))
    if msg == '<fool>':
        await message.channel.send('HOW DARE YOU!?!?!?!? YOU FOOLED ME!!!!!!')
        while True:
            await message.author.send('You fooled me!')
    if msg == '<revenge>':
        await message.channel.send(
            'https://www.youtube.com/watch?v=sSSOG8g7PFg')
    if msg == '<troll>':
        await message.channel.send('You have been trolled.')
        await message.author.send('https://www.youtube.com/watch?v=gvYfRiJQIX8'
                                  )
    if msg == '<redeem SPECIALPERSONWITHCOOLCODE>':
        await message.channel.send('Thanks! You get the platnim role!')
    if msg == '@durpy_pixel':
        while True:
            await message.author.send("Don't ping him!")
    if msg == 'UwU' or msg == 'uwu':
        await message.reply('OwO')
    if any(word in msg for word in bad_words):
        await message.delete()
        await message.channel.send('Message contains profanity')
    if get(message.author.roles, name="Server Operator"
           ) and "<lockdown_initiate>" in message.content.lower():
        await message.reply(
            'Lockdown initiated, to raise dm Major_Bozzy#7030 containing: code: 18.'
        )
        while True:
            if msg.startswith(''):
                await message.delete()


keep_alive()
try:
    client.run(bot_token)
except discord.HTTPException as e:
    if e.status == 429:
        print(
            "The Discord servers denied the connection for making too many requests"
        )
        print(
            "Get help from https://stackoverflow.com/questions/66724687/in-discord-py-how-to-solve-the-error-for-toomanyrequests"
        )
    else:
        raise e
