import discord
import random
from discord.ext import commands
listok = []
TOKEN = 'NzcxOTkzOTI5MjgxMTc1NjAy.X50NXw.apT66sMXaojNSdduBMgTQ0xR9N0'
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_message(message:discord.Message):
    id = message.author.id
    await ctx.send(id) 
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
@commands.has_any_role(779025466522468423)
async def giverole(ctx):
    await ctx.send("у вас есть роль")
    
bot.run(TOKEN)
