import discord
import asyncio
import random
from pythonping import ping
from discord.ext import commands

deltime = 90
cpfileclock = 0
cutepic = []


class General(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def please(self, ctx, *args):
        input1 = ''
        try:
            input1 = args[0]
        except:
            pass
        if input1 == 'help.':
            print(ctx.author.name+" Used please help")
            await ctx.send('>>> **General Commands**\nimage\ngenshin help\nroll\nhm help //(HangMan)\nping [Address] //(eg. google.com)\nmg help//(Mini-Games)\nmusic help', delete_after=30)
        await asyncio.sleep(10.5)
        await ctx.message.delete()

    @commands.command()
    async def ping(self, ctx, *args):
        print(ctx.author.name+" Used ping")
        input1 = ''
        try:
            input1 = args[0]
        except:
            pass

        if input1 == '':
            pass
        else:
            try:
                r = ping(input1, verbose=False)
                print(r)
                await ctx.send('>>> Ping successful to '+input1+' (' + str(r.rtt_avg_ms)+' ms)', delete_after=15)
            except:
                await ctx.send('>>> '+input1+' cannot be Pinged', delete_after=15)
        await asyncio.sleep(15.5)
        await ctx.message.delete()

    @commands.command()
    async def roll(self, ctx, *args):
        try:
            x = int(args[0])
        except:
            x = 10
        rollout = random.randrange(x)+1
        strrollout = "You have rolled "+str(rollout)+"/"+str(x)
        await ctx.send('>>> **'+strrollout+'**', delete_after=10)
        await asyncio.sleep(10)
        await ctx.message.delete()

    @commands.command()
    async def image(self, ctx, *args):
        print(ctx.author.name+" Used image")
        global cpfileclock
        if cpfileclock == 0:
            cpfileclock = 1
            with open('cutepictures.txt') as read_file:
                for line in read_file:
                    cutepic.append(line)
        await ctx.send('https://i.imgur.com/'+str(random.choice(cutepic)), delete_after=deltime)
        await asyncio.sleep(deltime)
        await ctx.message.delete()

    @commands.command()
    async def iimport(self, ctx, *args):
        print(ctx.author.name+" Used iimport")
        try:
            with open('cutepictures.txt') as read_file:
                for line in read_file:
                    cutepic.append(line)
            imagelink = []
            imagelink = str(args[0]).split("https://")
            del imagelink[0]
            imagelink = str(imagelink[0]).split("i.imgur.com/")
            del imagelink[0]
            count = 0
            for line in cutepic:
                if str(line) == str(imagelink[0]):
                    count = 1
            if count == 0:
                file = open('cutepictures.txt', 'a')
                file.write("\n"+imagelink[0])
                file.close()
                await ctx.send('>>> **'+imagelink[0]+'** Saved!', delete_after=10)
            else:
                await ctx.send('>>> **'+imagelink[0]+'** Is a duplicate', delete_after=10)
            await asyncio.sleep(10)
            await ctx.message.delete()
        except:
            await ctx.send('>>> **Wrong Format**', delete_after=10)
            await asyncio.sleep(10)
            await ctx.message.delete()


def setup(client):
    client.add_cog(General(client))
