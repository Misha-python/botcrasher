import discord
import random
from discord.ext import commands
listok = ["w","d"]
TOKEN = 'NzcxOTkzOTI5MjgxMTc1NjAy.X50NXw.apT66sMXaojNSdduBMgTQ0xR9N0'
bot = commands.Bot(command_prefix='l!')
@bot.event
async def on_ready():
    ctx.send("к бою гатов")
    game = discord.Game("аккаунты")
    await bot.change_presence(status=discord.Status.idle, activity=game)
@bot.group(invoke_without_command=True)
async def give(ctx):  # создаем асинхронную фунцию бота
    await ctx.send('нало')
@give.command()
async def minecraft(ctx):
    idd = ctx.message.author.id
   
    if idd == 704560097610825828:
        
        embed=discord.Embed(title="Тест ", description="Это ембдед. Лц:" +random.choice(listok), color=0x00ff00)
        embed.set_author(name="Боб")
        await ctx.send(embed=embed)
  # отправляем обратно аргумент
    else:
        await ctx.author.send("не хубка")
@bot.command(pass_context=True)
async def all(ctx):  # создаем асинхронную фунцию бота
    idd2 = ctx.message.author.id
    
    if idd2 == 704560097610825828:
        await ctx.send(listok)  # отправляем обратно аргумn
        await ctx.send(*listok)
        await ctx.send("вот вся база")
    else:
        await ctx.author.send("не хубка")


            
       
    
    
bot.run(TOKEN)
