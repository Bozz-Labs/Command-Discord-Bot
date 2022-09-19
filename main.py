import discord
import random
from keep_alive import keep_alive
import os

bot_token = os.environ['bot token']

mean_things = ['Ur stupid', 'idiot', 'u look like shrek', 'ima render dummy.html', 'yur mom', 'PUT SOME CLOTHES ON!!!', 'your homework is EASY lol', 'I could do this forever!']

nice_things = ['You are cool!', 'You can do it!', 'I believe in you!', 'I ran out of nice things to say.']

client = discord.Client()

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
  if msg == '<hello>':
    await message.channel.send('Hello')
  if msg.startswith('guess what') or msg.startswith('Guess What') or msg.startswith('Guess what') or msg.startswith('guess What') or msg.startswith('GUESS WHAT'):
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
    await message.channel.send('https://www.youtube.com/watch?v=sSSOG8g7PFg')
  if msg == '<troll>':
    await message.channel.send('You have been trolled.')
    await message.author.send('https://www.youtube.com/watch?v=gvYfRiJQIX8')
    

keep_alive()
client.run(bot_token)
