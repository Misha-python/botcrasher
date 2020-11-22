import discord
import random
from discord.ext import commands
list=[]
TOKEN = 'NzcxOTkzOTI5MjgxMTc1NjAy.X50NXw.apT66sMXaojNSdduBMgTQ0xR9N0'
bot = commands.Bot(command_prefix='!')


@bot.command(pass_context=True)  # разрешаем передавать агрументы
async def give(ctx, arg):  # создаем асинхронную фунцию бота
    await ctx.send(random.choice(e))  # отправляем обратно аргумент
@bot.command(pass_context=True)
async def add(ctx, arg):  # создаем асинхронную фунцию бота
    await ctx.send("добавил"+arg)  # отправляем обратно аргумn
    list.append(arg)


bot.run(TOKEN)
