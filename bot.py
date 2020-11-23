import discord
import random
from discord.ext import commands
listok = []
TOKEN = 'NzcxOTkzOTI5MjgxMTc1NjAy.X50NXw.apT66sMXaojNSdduBMgTQ0xR9N0'
bot = commands.Bot(command_prefix='!')
@bot.command(pass_context=True)  # разрешаем передавать агрументы
async def give(ctx):  # создаем асинхронную фунцию бота
    idd = ctx.message.author.id
    if idd == "":
        await ctx.send(random.choice(listok))  # отправляем обратно аргумент
    else:
        await ctx.send("не хубка")
@bot.command(pass_context=True)
async def add(ctx, arg):  # создаем асинхронную фунцию бота
    await ctx.send("добавил: "+arg)  # отправляем обратно аргумn
    el=arg
    listok.append(el)
    f = open("accs.txt","r+")
    ctx.send(*f)
    data = f.read()
    ctx.send(data)


            
       
    
    
bot.run(TOKEN)
