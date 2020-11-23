import discord
import random
from discord.ext import commands
listok = []
TOKEN = 'NzcxOTkzOTI5MjgxMTc1NjAy.X50NXw.apT66sMXaojNSdduBMgTQ0xR9N0'
bot = commands.Bot(command_prefix='l!')
@bot.command(pass_context=True)  # разрешаем передавать агрументы
async def give(ctx):  # создаем асинхронную фунцию бота
    await ctx.send(random.choice(listok))  # отправляем обратно аргумент
@bot.command(pass_context=True)
async def add(ctx, arg):  # создаем асинхронную фунцию бота
    await ctx.send("добавил: "+arg)  # отправляем обратно аргумn
    el=arg
    listok.append(el)
    f = open("accs.txt","r+")
    ctx.send(*f)
    data = f.read()
    ctx.send(data)
    ctx.send("нет доступа")
@bot.command(pass_context=True)
def sponge(ctx):
    idd=ctx.message.author.id
    if idd == 704560097610825828:
        await ctx.send("ты губка боб] твой id "+idd)
    else:
        await ctx.send("не губкам слова не давали! твой id "+idd)
    
    
bot.run(TOKEN)
