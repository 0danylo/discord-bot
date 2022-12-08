import asyncio
import datetime
import random
import time
from datetime import datetime
from datetime import timedelta

import discord
from discord.ext import tasks
from dotenv import load_dotenv

load_dotenv()
TOKEN = ''
GUILD = 638061170917507074

client = discord.Client(intents=discord.Intents.all())
botName = 'Counter'
counter = 0
count = 0

d1 = client.get_user(201445861228544000)
j1 = client.get_user(244191954156519426)
j2 = client.get_user(365210741474852864)
z = client.get_user(133070198067429376)
a = client.get_user(265953455238152195)
j3 = client.get_user(183602483434749952)
d2 = client.get_user(228972103582351362)
l = client.get_user(297120083430342656)
s = client.get_user(381965852758769667)
r = client.get_user(638059507813187605)

users = [d1, j1, j2, z, a, j3, d2, l, s, r]

esmBot = client.get_user(429305856241172480)
noble = client.get_user(804087125070839910)
bot = client.get_user(806730043694907402)
rythm = client.get_user(235088799074484224)

vc = None

ROLLS = 10
LUCK = 0.5

testing = False
notStupid = False
connected = False

messages = []
playlists = ['']

balances = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


@client.event
async def on_member_join(member):
   wasBanned = False
   if member.id == 439205512425504771:
      await client.guilds.pop(1).ban(member, reason=':neutral_face:')
      wasBanned = True
   print(wasBanned)


@client.event
async def on_ready():
   print("Ready")
   
   await client.change_presence(
      activity=discord.Activity(type=discord.ActivityType.playing, name='the game'))
   
   discord.VoiceClient(client, None)
   for cl in client.voice_clients:
      await cl.disconnect()
   
   print('Counting Messages...', end='', flush=True)
   for item in await client.get_channel(816866065090084884).history(limit=2500).flatten():
      if item.author == bot:
         count += 1
   print(str(count))
   
   print('Mining DanyloCoin...')
   cave = client.get_channel(830966914280587355)
   mining = await cave.history(limit=25000).flatten()
   
   for item in mining:
      if len(item.embeds) > 0 and len(item.embeds[0].fields) > 0 and \
            item.embeds[0].fields[0].title == 'DanyloCoin Mining':
         print(item.embeds)
         catch = item.embeds[0].fields[0].value[:-4]
         miner = item.embeds[0].author
         print(catch)
         print(miner)
         balances[users.index(miner)] += float(catch)
   
   print('Money Processed')
   print('Reading Messages...')
   startTime = datetime.now()
   
   for chan in client.guilds.pop(1).text_channels:
      print('#' + chan.name + '...', flush=True)
      for item in await chan.history(limit=100000).flatten():
         messages.append(item)
   
   endTime = datetime.now()
   print('Done in ' + str(endTime - startTime))


@client.event
async def on_massage_delete(mess):
   if not mess.author.bot and mess.channel != client.get_channel(815391777908588575):
      messtime = mess.created_at
      content = 'From #' + '**' + mess.channel.name + '**:\n' + \
                mess.author.name + ' at *' + str(messtime - timedelta(hours=5))[:-7] + '*:\n' + mess.content + '\n'
      await client.get_channel(815391777908588575).send(content)
      for item in mess.attachments:
         await client.get_channel(815391777908588575).send(item.proxy_url)
      messages.remove(mess)


@client.event
async def on_raw_message_delete(payload):
   global messages
   mess = next((item for item in messages if item.id == payload.message_id), None)
   
   if mess is not None and not mess.author.bot and mess.channel != client.get_channel(815391777908588575):
      messtime = mess.created_at
      content = 'From #' + '**' + mess.channel.name + '**:\n' + \
                mess.author.name + ' at *' + str(messtime - timedelta(hours=5))[:-7] + '*:\n' + mess.content + '\n'
      await client.get_channel(815391777908588575).send(content)
      for item in mess.attachments:
         await client.get_channel(815391777908588575).send(item.proxy_url)
      messages.remove(mess)


@client.event
async def on_voice_state_update(member, before, after):
   if member in users:
      mess = ''
      if before.channel is None and after.channel is not None:
         mess = '**' + member.name + '** joined **' + after.channel.name + \
                '**' + ' in ' + '**' + after.channel.guild.name + '**'
      elif before.channel is not None and after.channel is None:
         mess = '**' + member.name + '** left **' + before.channel.name + \
                '** in **' + before.channel.guild.name + '**'
      elif before.channel is not after.channel:
         mess = '**' + member.name + '** left **' + before.channel.name + \
                '** in **' + before.channel.guild.name + '** and joined **' + \
                after.channel.name + '** in **' + after.channel.guild.name + '**'
      
      if mess != '':
         await client.get_channel(822967463338835998).send(mess)


@tasks.loop(minutes=1)
async def dblsend():
   ct = datetime.now()
   if ct.hour == 13 and ct.minute == 49:
      await client.get_channel(752926316587778068).send('https://tenor.com/view/leonardo-di-caprio-cheers-great'
                                                        '-gatsby-gif-10577278')


@dblsend.before_loop
async def before():
   await client.wait_until_ready()


@client.event
async def on_message(message):
   
   global testing, notStupid, connected, count, counter, playlists
   global esmBot, noble, bot
   global vc
   
   if message.guild == client.guilds.pop(1):
      messages.append(message)
   if message.author == client.user:
      return
   
   cont = message.content.lower().replace(' ', '')
   
   if ('test' in cont or '21' in cont) and not testing and not notStupid:
      notStupid = False
      await message.channel.send('You stupid')
      testing = True
   elif testing and not notStupid:
      await message.channel.send('What\'s 9 + 10?')
      notStupid = True
   elif not ('19' in cont) and testing and notStupid:
      await message.channel.send('You stupid!')
      testing = False
      notStupid = False
   elif '19' in cont and testing and notStupid:
      await message.channel.send('You smart!')
      testing = False
      notStupid = False
   
   gifs = ['https://media.discordapp.net/attachments/795574373963792385/804378765689094204/image0.gif',
           'https://media.discordapp.net/attachments/734891737436389439/758095251394134056/image0.gif',
           'https://media.discordapp.net/attachments/623268814590574604/671570427356905492/babie-1.gif',
           'https://cdn.discordapp.com/emojis/697995591921172532.gif?',
           'https://cdn.discordapp.com/emojis/668687740421931028.gif?v=1',
           'https://media.discordapp.net/attachments/386150235103035392/641482848695746610/drive.gif',
           'https://media.discordapp.net/attachments/747579998856151102/749842356810940537/569722794737270794.gif',
           'https://media.discordapp.net/attachments/710605631840583823/763847396563615785/image0.gif',
           'https://media.discordapp.net/attachments/339070814986960897/776805739686920203/image0-44-1.gif',
           'https://cdn.discordapp.com/attachments/626752500321746946/670680034083602463/20200121_162129.gif',
           'https://cdn.discordapp.com/emojis/754633140617609247.gif?v=1',
           'https://cdn.discordapp.com/emojis/812786521211666483.gif?v=1',
           'https://cdn.discordapp.com/emojis/754339831676534925.gif?v=1',
           'https://cdn.discordapp.com/emojis/789713817252397106.gif?v=1',
           'https://media.discordapp.net/attachments/740318336302448701/814096807986331688/image0-4.gif',
           'https://media.discordapp.net/attachments/783008960982155274/847569317645385760/speed.gif']
   
   if cont == 'https://tenor.com/view/leonardo-di-caprio-mondays-inception-beach-days-gif-13539604':
      if datetime.today().weekday() == 0:
         await message.channel.send(
            'https://tenor.com/view/when-it-monday-walking-walking-in-circles-gif-15957675')
      elif datetime.today().weekday() == 1:
         await message.channel.send(
            'https://tenor.com/view/when-it-tuesday-when-it-tuesday-gif-20639130')
      elif datetime.today().weekday() == 2:
         await message.channel.send(
            'https://tenor.com/view/when-it-wednesday-chill-waking-back-walking-gif-17460902')
      elif datetime.today().weekday() == 3:
         await message.channel.send('https://tenor.com/view/when-it-thursday-thursday-walking-pink-man-gif-17460927')
      elif datetime.today().weekday() == 4:
         await message.channel.send('https://tenor.com/view/when-it-friday-meme-gif-gif-20140675')
      elif datetime.today().weekday() == 5:
         await message.channel.send('https://tenor.com/view/when-it-saturday-walking-tired-falling-gif-17460944')
      elif datetime.today().weekday() == 6:
         await message.channel.send('https://tenor.com/view/when-it-sunday-walking-chill-animation-gif-17460936')
   
   if 'gif' in cont:
      await message.channel.send(gifs[int(random.random() * len(gifs))])
   
   if message.guild == client.get_guild(638061170917507074):
      count += 1
      await client.get_channel(816866065090084884).send(
         'GIF #' + str(count) + ' goes to ' + message.author.mention)
   
   if 'mine' in cont and not message.author.bot and (message.channel == client.get_channel(830966914280587355) or
                                                     message.channel == client.get_channel(833118513106911332)):
      mess = mine(message.author)
      embed = discord.Embed(title="DanyloCoin Mining", color=0x3c33ed, author=message.author)
      embed.add_field(name=message.author.name + '\'s Mine', value=mess)
      await message.channel.send(embed=embed)
   
   if cont == 'ping' and not message.author.bot:
      message.channel.send('Pinging...')
      iMillis = float(time.time() * 1000)
      await client.get_channel(831007074330345482).send('ping')
      fMillis = float(time.time() * 1000)
      ping = fMillis - iMillis
      await message.channel.send(f"{ping:.0f}" + ' ms')
   
   if 'bank' in cont and not message.author.bot and (message.channel == client.get_channel(830992251378204673) or
                                                     message.channel == client.get_channel(831007074330345482) or
                                                     message.channel == client.get_channel(833152163650863173)):
      bal = balances[users.index(message.author)]
      subject = message.author.name
      
      if len(cont) > 4 and message.channel == client.get_channel(831007074330345482):
         subject = users[int(cont[4:])].name
         bal = balances[int(cont[4:])]
      
      embed = discord.Embed(title="DanyloBank", color=0x3c33ed, author=message.author)
      embed.add_field(name=subject + '\'s Account: ', value=(f"{bal:.60f}" if bal > 0 else '0') + ' DanyloCoin')
      await message.channel.send(embed=embed)
   
   if cont[:4] == 'give' and message.channel == client.get_channel(831007074330345482):
      index = int(cont[4])
      deposit = float(cont[5:])
      balances[index] += deposit
      await client.get_channel(831007074330345482).send(str(deposit) + ' DAC given to ' + users[index].name)
   elif 'lol' in cont and message.channel != client.get_channel(815391777908588575):
      if message.guild == client.get_guild(638061170917507074):
         count += 1
         await client.get_channel(816866065090084884).send(
            'lol #' + str(count) + ': ' + message.author.mention)
      await message.channel.send('shut up')
      for cl in client.voice_clients:
         if cl == message.author.voice.channel.connect() and not cl.is_connected():
            try:
               vc = await message.author.voice.channel.connect()
               if message.guild == client.get_guild(745005017899073537):
                  while True:
                     vc.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source="peter.mp3"))
                     await asyncio.sleep(6)
               elif message.author.voice.channel.connect().is_connected():
                  vc.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source="peter.mp3"))
            except AttributeError:
               pass
   elif 'shutup' in cont:
      await message.channel.send('lol')
      for cl in client.voice_clients:
         if cl.guild == message.guild:
            await cl.disconnect()
   
   if cont == 'ok' and message.author == client.get_user(297120083430342656):
      counter += 1
   
   if 'deez' in cont and ('nuts' in cont or 'nutz' in cont):
      counter += 1
   
   if 'count' in cont:
      await message.channel.send(counter)
   
   if 'fish' in cont:
      embed = discord.Embed(title="Epic Fishing", color=0x3c33ed, author=806730043694907402)
      mess = fish()
      embed.add_field(name=message.author.name + '\'s Catch', value=mess)
      await message.channel.send(embed=embed)
   
   if 'gaming' in cont or 'game' in cont:
      mess = ''
      dm = await message.author.create_dm()
      for p in playlists:
         mess += p + '\n'
         print(p)
      await dm.send(mess)
      await message.channel.send("mhm yep")


def fish():
   ALL_CHANCES = [0, 0.49, 0.723, 0.74, 0.851, 0.859, 0.867, 0.875, 0.883, 0.891, 0.899, 0.916, 0.926, 0.928, 0.938,
                  0.948, 0.958, 0.963, 0.968, 0.978, 0.988, 0.989, 0.999]
   ALL_VALUES = [1, 2.50, 30, 5, 10, 55, 10, 25, 100, 40, 0, 1.50, 2.50, 2, 8, 0, 0.50, 0.50, 2, 0, 2, 5]
   ALL_NAMES = ['Cod', 'Salmon', 'Clown Fish', 'Puffer Fish', 'Enchanted Bow', 'Enchanted Book',
                'Enchanted Fishing Rod', 'Name Tag', 'Nautilus Shell', 'Saddle', 'Lily Pad', 'Bowl', 'Fishing Rod',
                'Leather', 'Leather Boots', 'Rotten Flesh', 'Stick', 'String', 'Water Bottle', 'Bone', 'Ink Sac',
                'Tripwire Hook']
   
   fish_counts = [0] * len(ALL_NAMES)
   for i in range(ROLLS):
      if random.random() >= LUCK:
         rand = random.random()
         
         i, index = 0, 0
         while rand > ALL_CHANCES[i + 1]:
            index += 1
         
         fish_counts[index] += 1
   
   mess = ''
   profit = 0
   for i in range(len(fish_counts)):
      if fish_counts[i] > 0:
         fishMoney = ALL_VALUES[i] * fish_counts[i]
         mess += str(fish_counts[i]) + ' ' + ALL_NAMES[i] + ': $' + ((str(fishMoney) + '0' if fishMoney %
                                                                                              int(fishMoney) > 0 else str(int(fishMoney))) if int(fishMoney) > 0 else '0' if fishMoney == 0
         else '0.50') + '\n'
         profit += fishMoney
   
   return mess + '\nValue: $' + ((str(profit) + '0' if profit % int(profit) > 0 else str(int(profit))) if profit > 0
                                 else '0')


def mine(miner):
   chance = random.random()
   catch = random.random() / 1000 if chance > 0.999 else \
      random.uniform(1 / 1000000000000000000000000000000000000000000000000000000,
                     1 / 1000000000000000000000000000000000000000000000000000000000) if chance > 0.001 else 0
   
   balances[users.index(miner)] += catch
   if miner == d1:
      balances[0] += catch
   elif miner == j1:
      balances[1] += catch
   elif miner == j2:
      balances[2] += catch
   elif miner == z:
      balances[3] += catch
   elif miner == a:
      balances[4] += catch
   elif miner == j3:
      balances[5] += catch
   elif miner == d2:
      balances[6] += catch
   elif miner == l:
      balances[7] += catch
   elif miner == s:
      balances[8] += catch
   
   return (f"{catch:.60f}" if catch > 0 else '0') + ' DAC'


dblsend.start()


client.run(TOKEN)
