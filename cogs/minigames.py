import discord
import asyncio
import random
from discord.ext import commands
deltime = 90
ttticons = [':regional_indicator_x:',':o2:',':white_large_square:']
tttboardc = []
tttplayers = []
tttcplayer = 1
tttcurrent = False


class Mgames(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def mg(self, ctx, *args):
        global tttcurrent
        global tttboardc
        global tttcplayer
        tttboardo = ""
        inputc = ''
        inputc2 = ''
        input1 = ''
        try:
            inputc = args[0]
            inputc2 = args[1]
            input1 = args[2]
        except:
            pass
        if inputc == 'help':
            print(ctx.author.name+" Used mg help")
            await ctx.send('>>> **Commands**\nmg help\nmg ttt help\n', delete_after=10)
        if inputc == 'ttt':
            if inputc2 == 'help':
                print(ctx.author.name+" Used mg ttt help")
                await ctx.send('>>> **Minigames Commands**\nmg ttt start [@someone]\nmg ttt p //to place tile\nmg ttt stop //stops the current game', delete_after=30)
            if inputc2 == 'start':
                print(ctx.author.name+" Used mg ttt start")
                checkplayer2 = True
                user = ''
                if tttcurrent:
                    return
                try:
                    autherid = input1.split("!")
                    del autherid[0]
                    autherid = str(autherid[0]).split(">")
                    del autherid[1]
                    user = autherid[0]
                except:
                    checkplayer2 = False
                if str(user) == str(ctx.message.author.id):
                    checkplayer2 = False
                if not checkplayer2:
                    await ctx.send('There is no Player2', delete_after=10)
                    await asyncio.sleep(10.5)
                    await ctx.message.delete()
                    return
                tttboardc = [2,2,2,2,2,2,2,2,2]
                tttplayers.append(str(ctx.message.author.id))
                tttplayers.append(str(user))
                counting = 0
                for icons in tttboardc:
                    if counting == 3:
                        counting = 0
                        tttboardo = tttboardo+"\n"+ttticons[icons]
                    else:
                        tttboardo = tttboardo+ttticons[icons]
                    counting = counting + 1
                tttcurrent = True
                tttcplayer = random.randrange(2)
                await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Tic Tac Toe"))
                await ctx.send(tttboardo, delete_after=180)
                await ctx.send('<@!'+str(tttplayers[tttcplayer])+'> Its is your turn type <@!'+str(self.client.user.id)+'>. Use mg ttt p (1-9) to place at the location', delete_after=180)
            elif inputc2 == 'p':
                print(ctx.author.name+" Used mg ttt p")
                if not tttcurrent:
                    await ctx.send('There is not Tic Tac Toe game ongoing', delete_after=10)
                    return
                else:
                    if str(ctx.message.author.id) not in tttplayers:
                        await ctx.send('You are not in the game', delete_after=10)
                        return
                    elif str(ctx.message.author.id) != str(tttplayers[tttcplayer]):
                        await ctx.send('It is not your turn yet', delete_after=10)
                        return
                    else:
                        if len(input1) != 1:
                            await ctx.send('Please only use 1-9', delete_after=10)
                            return
                        elif int(input1) == 0:
                            await ctx.send('Please only use 1-9', delete_after=10)
                            return
                        else:
                            try:
                                testx = int(input1)
                            except:
                                await ctx.send('Please only use 1-9', delete_after=10)
                                return
                            if tttboardc[testx-1] == 2:
                                tttboardc[testx-1] = int(tttcplayer)
                                counting = 0
                                tttboardo = ''
                                checkwin = 0
                                countdraw = 0
                                for icons in tttboardc:
                                    if icons != 2:
                                        countdraw = countdraw+1
                                    if counting == 3:
                                        counting = 0
                                        tttboardo = tttboardo+"\n"+ttticons[icons]
                                    else:
                                        tttboardo = tttboardo+ttticons[icons]
                                    counting = counting + 1
                                if countdraw == 9:
                                    checkwin = 2
                                elif tttboardc[0] == tttboardc[1] == tttboardc[2] == tttcplayer:
                                    checkwin = 1
                                elif tttboardc[3] == tttboardc[4] == tttboardc[5] == tttcplayer:
                                    checkwin = 1
                                elif tttboardc[6] == tttboardc[7] == tttboardc[8] == tttcplayer:
                                    checkwin = 1
                                elif tttboardc[0] == tttboardc[3] == tttboardc[6] == tttcplayer:
                                    checkwin = 1
                                elif tttboardc[1] == tttboardc[4] == tttboardc[7] == tttcplayer:
                                    checkwin = 1
                                elif tttboardc[8] == tttboardc[5] == tttboardc[8] == tttcplayer:
                                    checkwin = 1
                                elif tttboardc[0] == tttboardc[4] == tttboardc[8] == tttcplayer:
                                    checkwin = 1
                                elif tttboardc[2] == tttboardc[4] == tttboardc[6] == tttcplayer:
                                    checkwin = 1
                                await ctx.send(tttboardo, delete_after=180)
                                if checkwin == 1:
                                    await ctx.send(':medal:<@!'+str(tttplayers[tttcplayer])+'> Has won this game!:medal:', delete_after=180)
                                elif checkwin == 2:
                                    await ctx.send('Game ended no one won :cry:', delete_after=180)
                                else:
                                    if int(tttcplayer) == 0:
                                        tttcplayer = 1
                                    else:
                                        tttcplayer = 0
                                    await ctx.send('<@!'+str(tttplayers[tttcplayer])+'> Its is your turn type mg ttt p (1-9) to place at the location', delete_after=180)
                                    #await ctx.send('<@!'+str(tttplayers[tttcplayer])+'> Its is your turn type <@!'+str(self.client.user.id)+'> mg ttt p (1-9) to place at the location', delete_after=180)
                                if checkwin != 0:
                                    await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Music"))
                                    tttcurrent = False
                                    tttcplayer = []
                            else:
                                await ctx.send('That slot is already taken', delete_after=10)
                                return
            elif inputc2 == 'stop':
                print(ctx.author.name+" Used mg ttt stop")
                await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Music"))
                await ctx.send('Stopping current Tic Tac Toe game', delete_after=10)
                tttcurrent = False
                tttcplayer = []

        await asyncio.sleep(10.5)
        await ctx.message.delete()


def setup(client):
    client.add_cog(Mgames(client))
