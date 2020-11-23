import discord
import random
from discord.ext import commands
listok = []
TOKEN = 'NzcxOTkzOTI5MjgxMTc1NjAy.X50NXw.apT66sMXaojNSdduBMgTQ0xR9N0'
bot = commands.Bot(command_prefix='!')
@bot.event
async def on_ready():
    while true:
        game = discord.Game("тут твой текст, который будет отображаться в Играет в")
        await bot.change_presence(status=discord.Status.idle, activity=game)
@bot.command(pass_context=True)  # разрешаем передавать агрументы
async def give(ctx):  # создаем асинхронную фунцию бота
    await ctx.send(random.choice(e))  # отправляем обратно аргумент
@bot.command(pass_context=True)
async def add(ctx, arg):  # создаем асинхронную фунцию бота
    await ctx.send("добавил"+arg)  # отправляем обратно аргумn
    el=arg
    listok.append("el")


bot.run(TOKEN)
