import discord
import asyncio
import random
from discord.ext import commands

charanimelist = []  # 1
randomqx = ""
answer = []
score = 0
fullscore = 0
question = ""
gamestarted = 0

class Trivia(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def t(self, ctx, *args):
        global gamestarted
        global charanimelist
        global question
        global answer
        global score
        global fullscore
        global randomqx
        command = ""
        print(answer)
        try:
            command = args[0]
        except:
            pass
        if command == "achar":
            if gamestarted != 0:
                await ctx.send('>>> **There is already a Trivia game going on**', delete_after=30)
            else:
                gamestarted = 1
                answer = []
                charanimelist = []
                question = ""
                randomqx = ""
                fullscore = 0
                score = 0
                with open('achar.txt') as read_file:
                    for line in read_file:
                        clean_linex = line.split('\n')
                        clean_line = clean_linex[0]
                        charanimelist.append(clean_line)
                randomqx = str(random.choice(charanimelist))
                charanimelist.remove(randomqx)
                randomq = randomqx.split('|')
                question = randomq[1]
                try:
                    randomans = randomq[0].split(' ')
                    answer.append(randomans[0])
                    answer.append(randomans[1])
                    answer.append(randomans[2])
                    answer.append(randomans[3])
                    answer.append(randomq[0])
                except:
                    answer.append(randomq[0])
                fullscore += 1
                await ctx.send(question, delete_after=360)

        elif command == "atitle":
            if gamestarted != 0:
                await ctx.send('>>> **There is already a Trivia game going on**',delete_after=30)
            else:
                gamestarted = 2
                answer = []
                charanimelist = []
                question = ""
                randomqx = ""
                fullscore = 0
                score = 0
                with open('atitle.txt') as read_file:
                    for line in read_file:
                        clean_linex = line.split('\n')
                        clean_line = clean_linex[0]
                        charanimelist.append(clean_line)
                randomqx = str(random.choice(charanimelist))
                charanimelist.remove(randomqx)
                randomq = randomqx.split('|')
                question = randomq[0]
                try:
                    answer.append(randomq[1])
                    answer.append(randomq[2])
                except:
                    pass
                fullscore += 1
                await ctx.send(question, delete_after=360)

        else:
            if (' '.join(args)).lower() in map(str.lower, answer):
                score += 1
                randomqx = str(random.choice(charanimelist))
                charanimelist.remove(randomqx)
                randomq = randomqx.split('|')
                if gamestarted == 1:
                    await ctx.send(">>> Answer: " + answer[-1] + "\n:partying_face: Score " + str(score) + " / " + str(fullscore), delete_after=60)
                elif gamestarted == 2:
                    await ctx.send(">>> Answer: "+', '.join(answer)+"\n:partying_face: Score "+str(score)+" / "+str(fullscore), delete_after=60)
                answer = []
                if gamestarted == 1:
                    question = randomq[1]
                    try:
                        randomans = randomq[0].split(' ')
                        answer.append(randomans[0])
                        answer.append(randomans[1])
                        answer.append(randomans[2])
                        answer.append(randomans[3])
                        answer.append(randomq[0])
                    except:
                        answer.append(randomq[0])
                    fullscore += 1
                    await ctx.send(question, delete_after=360)
                elif gamestarted == 2:
                    question = randomq[0]
                    try:
                        answer.append(randomq[1])
                        answer.append(randomq[2])
                    except:
                        pass
                    fullscore += 1
                    await ctx.send(question, delete_after=360)

            elif command == "help":
                await ctx.send('>>> **Trivia Commands**\nt achar                  //anime characters\nt atitle                  //anime titles\nt [guess]                  //your guess',delete_after=30)

            elif command == "skip":
                randomqx = str(random.choice(charanimelist))
                charanimelist.remove(randomqx)
                randomq = randomqx.split('|')
                if gamestarted == 1:
                    await ctx.send(">>> Answer: " + answer[-1] + "\n:partying_face: Score " + str(score) + " / " + str(fullscore), delete_after=60)
                elif gamestarted == 2:
                    await ctx.send(">>> Answer: "+', '.join(answer)+"\n:partying_face: Score "+str(score)+" / "+str(fullscore), delete_after=60)
                answer = []
                if gamestarted == 1:
                    question = randomq[1]
                    try:
                        randomans = randomq[0].split(' ')
                        answer.append(randomans[0])
                        answer.append(randomans[1])
                        answer.append(randomans[2])
                        answer.append(randomans[3])
                        answer.append(randomq[0])
                    except:
                        answer.append(randomq[0])
                    fullscore += 1
                    await ctx.send(question, delete_after=360)
                elif gamestarted == 2:
                    question = randomq[0]
                    try:
                        answer.append(randomq[1])
                        answer.append(randomq[2])
                    except:
                        pass
                    fullscore += 1
                    await ctx.send(question, delete_after=360)

            elif command == "quit":
                percent = "{:.2f}".format(((score/(fullscore-1))*100))
                if gamestarted == 1:
                    await ctx.send(">>> Answer: " + answer[-1] + "\nFinal Score: "+str(score)+" / "+str(fullscore-1)+"   ("+str(percent)+"%)  :partying_face:", delete_after=60)
                elif gamestarted == 2:
                    await ctx.send(">>> Answer: "+', '.join(answer)+"\nFinal Score: "+str(score)+" / "+str(fullscore-1)+"   ("+str(percent)+"%)  :partying_face:", delete_after=60)
                answer = []
                question = ""
                gamestarted = 0
                fullscore = 0
                score = 0
                charanimelist = []
                titanimelist = []

        await asyncio.sleep(2)
        await ctx.message.delete()


def setup(client):
    client.add_cog(Trivia(client))
