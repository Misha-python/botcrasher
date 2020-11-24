import discord
import json
import requests
import random
from discord.ext import commands
gubki = [732571199913328691,704560097610825828] 
text='''
chandlerbarton04@gmail.com:Barton2004!
thomasjc@live.ca:16tHe19987
marcosg_94@hotmail.com:marcos1794
carisido1@aol.com:Cooper76!
kevinmadsen01@gmail.com:Streetbasket2002
loganp326@gmail.com:Slendy15
kierstin.sada1@gmail.com:chickentaters21
mathes.lol1@web.de:Dusty005005!
mayamesriani@yahoo.com:Mayamaya2
j.a.m.r.marceau@gmail.com:Legionasmany1
killerwaterbug@gmail.com:Sounders23!
laylalalovelyllama@yahoo.com:disneyfan6
tcbohls@live.com:Window99!jiml7@verizon.
kingturtle02@gmail.com:smoothie02
legendxmachina@gmail.com:TV052804*$
'''
listok = text.split ('\n')
TOKEN = 'NzcxOTkzOTI5MjgxMTc1NjAy.X50NXw.apT66sMXaojNSdduBMgTQ0xR9N0'
bot = commands.Bot(command_prefix='l!')
@bot.event
async def on_ready():
    game = discord.Game("аккаунты и четаблин")
    await bot.change_presence(status=discord.Status.idle, activity=game)
@bot.group(invoke_without_command=True)
async def give(ctx):  # создаем асинхронную фунцию бота
    await ctx.send('нало')
@give.command()
async def minecraft(ctx):
    idd = ctx.message.author.id
   
    if idd in gubki:
        
        embed=discord.Embed(title="Тест ", description='''Это ембдед. 
                            Лц:''' +random.choice(listok), color=0x00ff00)
        embed.set_author(name="Боб")
        await ctx.author.send(embed=embed)
  # отправляем обратно аргумент
    else:
        await ctx.author.send("не хубка")
@bot.command(pass_context=True)
async def all(ctx):  # создаем асинхронную фунцию бота
    idd2 = ctx.message.author.id
    
    if idd2 == 704560097610825828 or idd2 == 732571199913328691:
         # отправляем обратно аргумn
        await ctx.send(listok)
        await ctx.send("вот вся база")
    else:
        await ctx.author.send("не хубка")

@bot.command()
async def fox(ctx):
    response = requests.get('https://some-random-api.ml/img/fox') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color = 0xff9900, title = 'лисичка) ') # Создание Embed'a
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    await ctx.send(embed = embed)
            
       
    
    
bot.run(TOKEN)
