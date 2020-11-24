import discord
import random
import json
import requests
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
from asyncio import sleep
@bot.event
async def on_ready():
    game = discord.Game("l!meme")
    game2 = discord.Game("l!help")
    While True:
        await bot.change_presence(status=discord.Status.idle, activity=game)
        await sleep(15)
        await bot.change_presence(status=discord.Status.idle, activity=game2)
        await sleep(15)
@bot.group(invoke_without_command=True)
async def give(ctx):  # создаем асинхронную фунцию бота
    await ctx.send('нало')
@give.command()
async def minecraft(ctx):
    idd = ctx.message.author.id
   
    if idd in gubki:
        
        embed = discord.Embed(title="твоя лицезния майнкрафт. кликни по мне, чтобы перейти на скачивание оффициального лаунчера", colour=discord.Colour(0xabd10f), url="https://www.minecraft.net/ru-ru/download", description='''твоя лицуха. бери!!!
        
        ||'''+random.choice(listok)+'''||
        формат: логин:пароль''')

        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/779025471252856852/780774815153520670/1606221592221_scale_1200.jpg")
        embed.set_footer(text="bot by spongebob | acc free", icon_url="https://cdn.discordapp.com/attachments/779025471252856852/780774814687297586/1604169731070_i.jpg")

        embed.add_field(name="🤔 что, если лц не сработает?", value="заменим ее!")
        embed.add_field(name="а откуда вы их берете?", value="это секрет, но незаконного ничего!", inline=True)
        embed.add_field(name="а сколько я могу получить?", value="безлимитно. приглашай!", inline=True)
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

@bot.command(pass_context=True)
async def meme(ctx):
    response = requests.get('https://some-random-api.ml/meme') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embedfox = discord.Embed(color = 0xff9900, title = json_data['caption']) # Создание Embed'a
    embedfox.set_image(url = json_data['image']) # Устанавливаем картинку Embed'a
    await ctx.send(embed = embedfox)
    
    
bot.run(TOKEN)
