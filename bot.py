import discord
import random
from discord.ext import commands
listok = ["w","d"]
TOKEN = 'NzcxOTkzOTI5MjgxMTc1NjAy.X50NXw.apT66sMXaojNSdduBMgTQ0xR9N0'
bot = commands.Bot(command_prefix='l!')
@bot.group(invoke_without_command=True)
async def give(ctx):  # создаем асинхронную фунцию бота
    await ctx.send('нало')
@give.command()
async def minecraft(ctx):
    idd = ctx.message.author.id
   
    if idd == 704560097610825828:
        await ctx.author.send(random.choice(listok))  # отправляем обратно аргумент
    else:
        await ctx.author.send("не хубка")
@bot.command(pass_context=True)
async def all(ctx):  # создаем асинхронную фунцию бота
    idd2 = ctx.message.author.id
    
    if idd2 == 704560097610825828:
        await ctx.send(listok)  # отправляем обратно аргумn
        await ctx.send("вот вся база")
    else:
        await ctx.author.send("не хубка")
   

            
       
    
    
bot.run(TOKEN)
