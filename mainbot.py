import discord
from discord.ext import commands, tasks
import asyncio
import os
import random
import gspread
from datetime import date
from oauth2client.service_account import ServiceAccountCredentials

client = commands.Bot(command_prefix='<@!248426164643692544> ')
#client = commands.Bot(command_prefix='`')
token = 'MjQ4NDI2MTY0NjQzNjkyNTQ0.WCxS5Q.S38pv3iVqXF-1UFXEuSX4-oQGrA'
callbot = ''
deltime = 5
spamlist = []
client.remove_command('help')


@client.event
async def on_ready():
    global callbot
    print('Bot is now online')
    callbot = '<@!'+str(client.user.id)+'>'
    await client.change_presence(status=discord.Status.online)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Music"))


@tasks.loop(seconds=5)
async def spamming(ctx):
    outputx = '>>> '
    for each in spamlist:
        outputx = outputx + '<@!' + str(each) + '>'
    await ctx.send(outputx, delete_after=0.5)


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('>>> '+str(random.choice(['What?  :thinking:','Huh?  :thinking:','What?','Huh?','What is it?','What you want?','What talking you',':thinking:','What are you talking about?','Invalid command'])), delete_after=5)
        await asyncio.sleep(5.5)
        await ctx.message.delete()


@client.command()
async def spam(ctx, *args):
    print(ctx.author.name+" Used spam")
    input1 = ''
    try:
        input1 = args[0]
    except:
        pass
    if input1 == 'stop':
        try:
            for users in args:
                if users == 'stop':
                    pass
                else:
                    input2 = users
                    autherid = str(input2).split("!")
                    del autherid[0]
                    autherid = str(autherid[0]).split(">")
                    del autherid[1]
                    user = autherid[0]
                    spamlist.remove(user)
                    if len(spamlist) == 0:
                        spamming.stop()
                    await ctx.send('>>> Stopped Spamming <@!' + str(user) + '>', delete_after=10)
        except:
            pass

    elif input1 == 'list':
        listofspam = 'Spam List'
        for each in spamlist:
            listofspam = listofspam+'\n<@!'+str(each)+'>'
        await ctx.send('>>> '+listofspam+'', delete_after=10)

    else:
        try:
            input2 = args[0]
            autherid = str(input2).split("!")
            del autherid[0]
            autherid = str(autherid[0]).split(">")
            del autherid[1]
            user = autherid[0]
            for users in args:
                input2 = users
                autherid = str(input2).split("!")
                del autherid[0]
                autherid = str(autherid[0]).split(">")
                del autherid[1]
                user = autherid[0]
                checkdup = 0
                for each in spamlist:
                    if input1 == each:
                        checkdup = 1
                        break
                if checkdup == 0:
                    spamlist.append(user)
                    await ctx.send('>>> Started Spamming <@!' + str(user) + '>', delete_after=10)
                    spamming.start(ctx)
        except:
            pass
    await asyncio.sleep(10.5)
    await ctx.message.delete()


@client.command()
async def help(ctx):
    print(ctx.author.name+" Used help")
    await ctx.send('>>> No  :zany_face:', delete_after=5)
    await asyncio.sleep(5.5)
    await ctx.message.delete()


@client.command()
async def load(ctx, extension):
    print(ctx.author.name+" Used load")
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'>>> {extension} Cog loaded', delete_after=5)
    print(f'{extension} Cog loaded')
    await asyncio.sleep(5.5)
    await ctx.message.delete()


@client.command()
async def unload(ctx, extension):
    print(ctx.author.name+" Used unload")
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'>>> {extension} Cog unloaded', delete_after=5)
    print(f'{extension} Cog unloaded')
    await asyncio.sleep(5.5)
    await ctx.message.delete()


@client.command()
async def reload(ctx, extension):
    print(ctx.author.name+" Used reload")
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'>>> {extension} Cog reloaded', delete_after=5)
    print(f'{extension} Cog reloaded')
    await asyncio.sleep(5.5)
    await ctx.message.delete()


@load.error
async def load_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('>>> No such Cog', delete_after=5)
        await asyncio.sleep(5.5)
        await ctx.message.delete()


@unload.error
async def unload_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('>>> No such Cog', delete_after=5)
        await asyncio.sleep(5.5)
        await ctx.message.delete()


@reload.error
async def reload_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('>>> No such Cog', delete_after=5)
        await asyncio.sleep(5.5)
        await ctx.message.delete()


def is_it_me(ctx):
    return ctx.author.id == 237115678782390272


@client.command()
@commands.check(is_it_me)
async def fk(ctx, inputx):
    if inputx == 'off':
        await client.change_presence(status=discord.Status.offline)
        await ctx.send('>>> Okay :cry:\n\n' + str(client.user) + ' is now **Offline**',delete_after=5)
        await asyncio.sleep(5.5)
        await ctx.message.delete()
        exit()


@fk.error
async def fk_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await asyncio.sleep(5.5)
        await ctx.message.delete()


@client.command()
@commands.check(is_it_me)
async def leave(ctx):
    await client.change_presence(status=discord.Status.offline)
    await ctx.send('>>> Leaving\n\n' + str(client.user) + ' is now **Offline**',delete_after=5)
    await asyncio.sleep(5.5)
    await ctx.message.delete()
    exit()

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(token)
