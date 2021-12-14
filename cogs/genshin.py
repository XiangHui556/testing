import discord
import gspread
import asyncio
from discord.ext import commands
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('project-tester-222318-37d284d78c43.json', scope)

gc = gspread.authorize(credentials)

wks = gc.open('Wish Tracker').worksheet('Botdata')
wksb = gc.open('Wish Tracker').worksheet('Banner')
deltime = 120


class Genshin(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def genshin(self, ctx, *args):
        checkcall = args
        checkfunc = ''
        try:
            checkfunc = checkcall[0]  # save bot call function
        except:
            pass
        if checkfunc == "help":
            print(ctx.author.name+" Used genshin help")
            await ctx.send('>>> **Genshin Commands**\ngenshin help\ngenshin pity\ngenshin banner', delete_after=30)
        if checkfunc == "pity":
            print(ctx.author.name+" Used genshin pity")
            user_array = []
            try:
                autherid = str(checkcall[1]).split("!")
                del autherid[0]
                autherid = str(autherid[0]).split(">")
                del autherid[1]
                user = autherid[0]
            except:
                user = ctx.message.author.id

            with open('gpity.txt') as read_file:
                for line in read_file:
                    user_array.append(line)
            currentau = ""  # current user's row in sheet
            for elem in user_array:
                elemdata = elem.split('|')
                if str(elemdata[0]) == str(user):
                    currentau = elemdata[1]
                    break
            try:
                pity = []
                pity = wks.col_values(int(currentau))
                wishname = pity[0]
                del pity[:2]
                await ctx.send(
                    '>>> User: __**' + wishname + '**__\n\n__**Character Event Wish**__\n**4★**      **5★**\n' + pity[
                        0] + '          ' + pity[1] + '\n\n__**Weapon Event Wish**__\n**4★**      **5★**\n' + pity[
                        2] + '          ' + pity[3] + '\n\n__**Permanent Wish**__\n**4★**      **5★**\n' + pity[4] + '          ' +
                    pity[5], delete_after=deltime)

            except:
                await ctx.send('>>> **Nothing Found**', delete_after=deltime)

        if checkfunc == "banner":
            print(ctx.author.name+" Used genshin banner")
            try:
                bannerc = wksb.acell('B15').value
                bannerw = wksb.acell('B16').value
                enddate = wksb.acell('B17').value
                await ctx.send(str(bannerc), delete_after=deltime)
                await ctx.send(str(bannerw), delete_after=deltime)
                await ctx.send('>>> Banners ends on: '+enddate, delete_after=deltime)
            except:
                await ctx.send('>>> **Nothing Found**', delete_after=deltime)
        await asyncio.sleep(10.5)
        await ctx.message.delete()

def setup(client):
    client.add_cog(Genshin(client))
