import discord
import random
from discord.ext import commands

TOKEN = 'NzcxOTkzOTI5MjgxMTc1NjAy.X50NXw.apT66sMXaojNSdduBMgTQ0xR9N0'
bot = commands.Bot(command_prefix='!')

sp=['1','e','y','r','u','df','y','5','7','s']
@bot.command(pass_context=True)  # разрешаем передавать агрументы
async def test(ctx, arg):  # создаем асинхронную фунцию бота
    await ctx.send(random.choice(sp)  # отправляем обратно аргумент


bot.run(TOKEN)
