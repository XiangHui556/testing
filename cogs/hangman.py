import discord
import asyncio
import random
from discord.ext import commands
deltime = 90
cpfileclock = 0
hangmandef = []
allinputs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '`', '\'', '"', '/', '[', ']', '.', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ':', ';', '{', '}', '\\', '~', ',', '?', '+', '=', '-', '_', '<', '>']
lives = 0
currentgame = 0
underscore = "__  __"
guessedapl = []
mainwordlist = []
mainword = ""
gwordlist = []
rightword = []
gword = ""
genre = ''
hint = ''
crossedapl = ""
ogenre = ''
ohint = ''
lifeimage = []
lifeimage.append('>>> —————— Lives \n         |         |\n       ☻       |\n       /|\\      |\n         |         |\n       / \\      |\n                   |')
lifeimage.append('>>> —————— Lives ♥\n                   |\n       ☻       |\n       /|\\      |\n         |         |\n       / \\      |\n                   |')
lifeimage.append('>>> —————— Lives ♥♥\n                   |\n       ☻       |\n       /|\\      |\n         |         |\n       /          |\n                   |')
lifeimage.append('>>> —————— Lives ♥♥♥\n                   |\n       ☻       |\n       /|\\      |\n         |         |\n                   |\n                   |')
lifeimage.append('>>> —————— Lives ♥♥♥♥\n                   |\n       ☻       |\n       /|        |\n         |         |\n                   |\n                   |')
lifeimage.append('>>> —————— Lives ♥♥♥♥♥\n                   |\n       ☻       |\n         |         |\n         |         |\n                   |\n                   |')
lifeimage.append('>>> —————— Lives ♥♥♥♥♥♥\n                   |\n       ☻       |\n                   |\n                   |\n                   |\n                   |')
lifeimage.append('>>> —————— Lives ♥♥♥♥♥♥♥\n                   |\n                   |\n                   |\n                   |\n                   |\n                   |')
lifeimage.append('>>> —————— Lives ♥♥♥♥♥♥♥♥\n|\n|\n|\n|\n|\n|')


class Hangman(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def hm(self, ctx, *args):
        global cpfileclock
        global currentgame
        global mainword
        global mainwordlist
        global gword
        global gwordlist
        global rightword
        global genre
        global hint
        global ogenre
        global guessedapl
        global crossedapl
        global ohint
        global underscore
        global lives
        inputc = ''
        input1 = ''
        try:
            inputc = str(args[0]).lower()
            input1 = str(args[1]).lower()
        except:
            pass
        if cpfileclock == 0:
            cpfileclock = 1
            with open('hangmandef.txt') as read_file:
                for line in read_file:
                    clean_linex = line.split('\n')
                    clean_line = clean_linex[0]
                    hangmandef.append(clean_line)
        if inputc == 'help':
            print(ctx.author.name+" Used hm help")
            await ctx.send('>>> **HangMan Commands**\nhm start [Keyword] [Genre] [Hint]       //[  ] This are optional\nhm stop                                                        //Stops the current game\nhm g                                                          //Guess an Character', delete_after=30)
            await asyncio.sleep(20.5)
            await ctx.message.delete()

        if inputc == 'start':
            print(ctx.author.name+" Used hm start")
            if currentgame == 0:
                mainword = ''
                genre = ''
                hint = ''
                ogenre = ''
                ohint = ''
                guessedapl = []
                crossedapl = ''
                timer = 180.5
                if input1 == '':
                    randomqx = str(random.choice(hangmandef))
                    randomq = randomqx.split('|')
                    try:
                        mainword = str(randomq[0]).lower()
                        genre = randomq[1]
                        hint = randomq[2]
                    except:
                        pass
                else:
                    mainword = input1
                    timer = 0
                for apl in mainword:
                    mainwordlist.append(apl)
                    if apl == " ":
                        gwordlist.append(" ")
                    else:
                        gwordlist.append(underscore)
                currentgame = 1
                lives = 8
                gword = " ".join(gwordlist)
                await ctx.send('>>> New Hangman Game Started', delete_after=180)
                await ctx.send(lifeimage[lives], delete_after=180)
                await ctx.send('>>> Guess: '+gword+ogenre+ohint, delete_after=180)
                await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="HangMan"))
                await asyncio.sleep(timer)
                await ctx.message.delete()
            else:
                await ctx.send('>>> There is already a Hangman Game ongoing :face_with_raised_eyebrow:',delete_after=10)
                await asyncio.sleep(10.5)
                await ctx.message.delete()

        elif inputc == "g":
            print(ctx.author.name+" Used hm g")
            if len(input1) == 1:
                if currentgame == 0:
                    await ctx.send('>>> There is **No** Hangman Game Ongoing :man_facepalming:',delete_after=10)
                    await asyncio.sleep(10.5)
                    await ctx.message.delete()
                if input1 not in mainwordlist and rightword:
                    lives = lives - 1
                    guessedapl.append("~~ "+input1+" ~~")
                    crossedapl = ' '.join(guessedapl)
                    await ctx.send(lifeimage[lives], delete_after=180)
                    await ctx.send('>>> Guess: '+gword+ogenre+ohint+"\nWrongs: "+crossedapl, delete_after=180)
                    if lives == 6:
                        ogenre = "\nGenre: "+genre
                    if lives == 3:
                        if hint != "":
                            ohint = "\nHint: "+hint
                    if lives == 0:
                        await ctx.send('>>> **(You Lost)** Hangman Game Has Been Ended\nIt was: '+str(mainword)+ogenre+ohint, delete_after=180)
                        currentgame = 0
                        mainword = ''
                        genre = ''
                        hint = ''
                        gwordlist = []
                        mainwordlist = []
                        rightword = []
                        guessedapl = []
                        ogenre = ''
                        crossedapl = ''
                        ohint = ''
                        lives = 0
                        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Music"))
                else:
                    gwordlist = []
                    mainwordlist = []
                    rightword.append(input1)
                    for apl in mainword:
                        if apl not in rightword:
                            if apl == " ":
                                gwordlist.append(" ")
                            else:
                                mainwordlist.append(apl)
                                gwordlist.append(underscore)
                        else:
                            gwordlist.append("__"+apl+"__")
                    gword = " ".join(gwordlist)
                    await ctx.send(lifeimage[lives], delete_after=180)
                    if len(mainwordlist) == 0:
                        if len(crossedapl) == 0:
                            await ctx.send('>>> Guess: '+gword+ogenre+ohint, delete_after=180)
                        else:
                            await ctx.send('>>> Guess: '+gword+ogenre+ohint+"\nWrongs: "+crossedapl, delete_after=180)
                        await ctx.send('>>> **(:medal:You Won!:medal:)** Hangman Game Has Been Ended\nIt was: '+str(mainword)+ogenre+ohint, delete_after=180)
                        currentgame = 0
                        mainword = ''
                        genre = ''
                        hint = ''
                        gwordlist = []
                        mainwordlist = []
                        guessedapl = []
                        rightword = []
                        ogenre = ''
                        crossedapl = ''
                        ohint = ''
                        lives = 0
                        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Music"))
                    else:
                        if len(crossedapl) == 0:
                            await ctx.send('>>> Guess: ' + gword + ogenre + ohint, delete_after=180)
                        else:
                            await ctx.send('>>> Guess: ' + gword + ogenre + ohint + "\nWrongs: " + crossedapl, delete_after=180)
                await asyncio.sleep(180.5)
                await ctx.message.delete()
            elif currentgame == 0:
                await ctx.send('>>> There is **No** Hangman Game Ongoing :man_facepalming:',delete_after=10)
                await asyncio.sleep(10.5)
                await ctx.message.delete()

            else:
                await ctx.send('>>> Please only guess **One** Character :man_facepalming:',delete_after=10)
                await asyncio.sleep(10.5)
                await ctx.message.delete()

        elif inputc == "stop":
            if currentgame == 0:
                await ctx.send('>>> There is **No** Hangman Game Ongoing :man_facepalming:',delete_after=10)
                await asyncio.sleep(10.5)
                await ctx.message.delete()
            else:
                await ctx.send('>>> Hangman Game Has Been Stopped\nIt was: '+str(mainword)+ogenre+ohint, delete_after=60)
                currentgame = 0
                mainword = ''
                genre = ''
                hint = ''
                gwordlist = []
                mainwordlist = []
                guessedapl = []
                rightword = []
                crossedapl = ''
                ogenre = ''
                ohint = ''
                lives = 0
                await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Music"))
                await asyncio.sleep(60.5)
                await ctx.message.delete()


def setup(client):
    client.add_cog(Hangman(client))
