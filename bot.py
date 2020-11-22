import discord
import random
from discord.ext import commands
e=["1","2",'3',"4"]
TOKEN = 'NzcxOTkzOTI5MjgxMTc1NjAy.X50NXw.apT66sMXaojNSdduBMgTQ0xR9N0'
bot = commands.Bot(command_prefix='!')


@bot.command(pass_context=True)  # разрешаем передавать агрументы
async def test(ctx, arg):  # создаем асинхронную фунцию бота
    await ctx.send(random.choice(e))  # отправляем обратно аргумент


bot.run(TOKEN)
