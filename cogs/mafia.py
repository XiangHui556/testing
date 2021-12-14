import discord
import asyncio
import random
from discord.ext import commands
from discord import DMChannel

mafiacurrent = False
mafiastart = False
mafiaset = False
randokilllines = [" Was found **Burned** to dead :fire:"," Was found **Drowned** in a near by lake :droplet:"," Was found with multiple **Stab** wounds :knife:"," Was found **Burned** down along with his house :heart_on_fire:"," Was found with a *Gunshot* wound through the heart :drop_of_blood:"," Was found **Motionless**"," Was found **Dead**"," Was found **Dead** with his eyes wide open :eye::eye:"," Was found **Dead** in a Rubbish Bin :recycle:"," Was found **Dead** fully stripped of all his belonging"," Was found **Dead** from all the Math questions he was forced to do"," Was found **Ravaged** by Dogs"," Was found **Poisoned** :skull_crossbones:"," Was found **Sleeping** Forever."," Was found **Minced** up by a Chainsaw"," Was found **Minced** by a Shotgun"]
joinedplayer = []
joinedplayerid = []
aliveplayerid = []
mafia = []
mafiadone = []
nummafia = 0
civilian = []
doctor = []
doctordone = []
numdoc = 0
detective = []
detectivedone = []
numdetect = 0
pdead = []
hostid = ''
channeldef = ''
roommessage = ''
investigate = []
civiliandone = []
voting2 = []
voting = []
voted = []
killlist = []
heallist = []
timephase = 0
timenumber = 0
timenumber2 = 0
votingnumber = 0
messagem = ''
endgame = False


class Mafia(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def mafia(self, ctx, *args):
        global joinedplayer
        global joinedplayerid
        global aliveplayerid
        global mafia
        global nummafia
        global civilian
        global doctor
        global numdoc
        global detective
        global numdetect
        global pdead
        global mafiacurrent
        global roommessage
        global channeldef
        global mafiastart
        global mafiaset
        global hostid
        global timephase
        global timenumber
        global timenumber2
        global investigate
        global killlist
        global heallist
        global messagem
        global mafiadone
        global detectivedone
        global doctordone
        global civiliandone
        global voting
        global votingnumber
        global voted
        global endgame
        global voting2
        inputc = ''
        input1 = ''
        input2 = ''
        input3 = ''
        try:
            inputc = args[0]
            input1 = args[1]
            input2 = args[2]
            input3 = args[3]
        except:
            pass
        if inputc == 'help':
            print(ctx.author.name+" Used mafia help")
            await ctx.send('>>> **Mafia Commands**\nmafia create\nmafia join\nmafia start\nmafia set\nmafia kill\nmafia heal\nmafia invest\nmafia skip\nmafia vote\nmafia stopgame', delete_after=30)

        elif inputc == "create":
            if mafiacurrent:
                await ctx.send(">>> There is already a Mafia games Ongoing", delete_after=10)
                return
            print(ctx.author.name+" Used mafia create")
            mafiacurrent = True
            mafiastart = False
            mafiaset = False
            endgame = False
            joinedplayer = []
            joinedplayerid = []
            aliveplayerid = []
            investigate = []
            messagem = ''
            killlist = []
            heallist = []
            mafia = []
            voted = []
            voting2 = []
            nummafia = 0
            civilian = []
            doctor = []
            numdoc = 0
            detective = []
            mafiadone = []
            doctordone = []
            detectivedone = []
            civiliandone = []
            voting = []
            votingnumber = 0
            numdetect = 0
            timenumber = 0
            timenumber2 = 0
            pdead = []
            roommessage = ''
            channeldef = ''
            timephase = 0
            hostid = ctx.author.id
            channeldef = await self.client.fetch_channel(int(ctx.channel.id))
            await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Mafia: Creating Room"))
            joinedplayer.append(ctx.author.name)
            joinedplayerid.append(ctx.author.id)
            aliveplayerid.append(ctx.author.id)
            messagex = '>>> **Mafia Room (No. Players: '+str(len(joinedplayer))+')**\nUse mafia join to join room\n\n'+joinedplayer[-1]+"  (Host)"
            roommessage = await channeldef.send(messagex, delete_after=300)

        elif inputc == "join":
            if not mafiacurrent:
                await ctx.send(">>> There is no Mafia games going on", delete_after=10)
                return
            for cplayers in joinedplayerid:
                if ctx.author.id == cplayers:
                    await ctx.send(">>> You are already in the room", delete_after=20)
                    return
            if mafiastart:
                await ctx.send(">>> Its too late to join the game has already started", delete_after=10)
                return
            print(ctx.author.name+" Used mafia join")
            joinedplayer.append(ctx.author.name)
            joinedplayerid.append(ctx.author.id)
            aliveplayerid.append(ctx.author.id)
            messagex = '>>> **Mafia Room (No. Players: '+str(len(joinedplayer))+')**\nUse mafia join to join room\n'
            countx = 1
            for players in joinedplayer:
                if countx == 1:
                    countx = 0
                    messagex += "\n"+players + "  (Host)"
                else:
                    messagex += "\n"+players
            messagex += "\n\n"+joinedplayer[-1]+" Joined!"
            await roommessage.edit(content=messagex, delete_after=300)

        elif inputc == "stopgame":
            if not mafiacurrent:
                await ctx.send(">>> There is no Mafia games going on", delete_after=10)
            print(ctx.author.name+" Used mafia stopgame")
            await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Music"))
            mafiacurrent = False
            mafiastart = False
            mafiaset = False
            endgame = False
            joinedplayer = []
            joinedplayerid = []
            aliveplayerid = []
            investigate = []
            killlist = []
            heallist = []
            mafia = []
            nummafia = 0
            civilian = []
            mafiadone = []
            voted = []
            doctordone = []
            detectivedone = []
            civiliandone = []
            voting = []
            voting2 = []
            votingnumber = 0
            messagem = ''
            doctor = []
            numdoc = 0
            timenumber = 0
            timenumber2 = 0
            detective = []
            numdetect = 0
            pdead = []
            roommessage = ''
            channeldef = ''
            hostid = ''
            timephase = 0
            await ctx.send(">>> Mafia game stopped", delete_after=20)

        elif inputc == "start":
            if not mafiacurrent:
                await ctx.send(">>> There is no Mafia games going on", delete_after=10)
                return
            if mafiastart:
                await ctx.send(">>> There is already Mafia games going on", delete_after=10)
                return
            elif hostid == ctx.author.id:
                print(ctx.author.name+" Used mafia start")
                mafiastart = True
                await channeldef.send(">>> **Mafia game started!**\nCurrently in setting phase\nPlease indicate the number mafias, detectives, doctor (the rest will be civ)\nUsing \"mafia set\" eg.(mafia set 2 1 1) the rest will be Civ", delete_after=600)
            else:
                await ctx.send(">>> You are not the host of this game", delete_after=10)
                return

        elif inputc == "set":
            if hostid == ctx.author.id:
                if not mafiacurrent:
                    await ctx.send(">>> There is no Mafia games going on", delete_after=10)
                    return
                if not mafiastart:
                    await ctx.send(">>> There is Mafia Game is not started", delete_after=10)
                    return
                if mafiaset:
                    await ctx.send(">>> There is Mafia Game has already been set", delete_after=10)
                    return
                try:
                    nummafia = int(input1)
                    numdoc = int(input3)
                    numdetect = int(input2)
                except:
                    await ctx.send(">>> Please only input numbers eg. (mafia set 1 0 0)", delete_after=10)
                    return
                totalp = numdetect + numdoc + nummafia
                if nummafia == 0:
                    await ctx.send(">>> Why are you playing mafia with 0 mafias :thinking:", delete_after=10)
                    return
                if totalp > len(joinedplayer):
                    await ctx.send(">>> There are "+str(totalp)+" Roles, but only "+str(len(joinedplayer))+" Players", delete_after=10)
                    return
                else:
                    if len(joinedplayer) <= 3:
                        if nummafia <= 1:
                            pass
                        else:
                            await ctx.send(">>> There are too many mafia for only " + str(len(joinedplayer)) + " Players",delete_after=10)
                            return
                    elif len(joinedplayer) <= 7:
                        if nummafia <= 2:
                            pass
                        else:
                            await ctx.send(">>> There are too many mafia for only " + str(len(joinedplayer)) + " Players",delete_after=10)
                            return
                    elif len(joinedplayer) >= 8:
                        if nummafia <= 3:
                            pass
                        else:
                            await ctx.send(">>> There are too many mafia for only " + str(len(joinedplayer)) + " Players",delete_after=10)
                            return
                    else:
                        await ctx.send(">>> Some error happened try set again",delete_after=10)

                mafiaset = True
                await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Mafia"))
                messagem = "Your following **Mafia Member**:detective:: "
                print(ctx.author.name+" Used mafia set")
                for y in range(nummafia):
                    mmember = random.choice(joinedplayerid)
                    messagem = messagem + " <@!"+str(mmember)+">,"
                    mafia.append(mmember)
                    joinedplayerid.remove(mmember)
                if numdetect == 0:
                    pass
                else:
                    for y in range(numdetect):
                        demember = random.choice(joinedplayerid)
                        detective.append(demember)
                        joinedplayerid.remove(demember)
                if numdoc == 0:
                    pass
                else:
                    for y in range(numdoc):
                        domember = random.choice(joinedplayerid)
                        doctor.append(domember)
                        joinedplayerid.remove(domember)
                if not joinedplayerid:
                    pass
                else:
                    for y in joinedplayerid:
                        civilian.append(y)
                    joinedplayerid = []
                messagex = ">>> :crescent_moon: **Night 0 begins!** :crescent_moon:\n**Players Alive**:"
                await channeldef.send(">>> **Mafia Game Started**\n:detective:**Mafia**: "+str(len(mafia))+"\n:man_police_officer:**Detective**: "+str(len(detective))+"\n:health_worker:**Doctor**: "+str(len(doctor))+"\n:deaf_person:**Civilian**: "+str(len(civilian))+"\nEveryone should get a role from the bot through DM", delete_after=300)
                counter = 0
                for ap in aliveplayerid:
                    counter = counter + 1
                    messagex = messagex + "\n"+str(counter)+". <@!"+str(ap)+">"
                await channeldef.send(messagex, delete_after=600)

                for mm in mafia:
                    user = await self.client.fetch_user(mm)
                    await DMChannel.send(user,">>> **Mafia Game**\nYour role is The **Mafia** :detective:\n\n**Your moves:**\n1. mafia kill eg.(mafia kill 1 //will kill player 1)\n2. mafia skip       //Will skip tonight\nRemember to @ the bot before the commands",delete_after=1800)
                    await DMChannel.send(user,messagex + "\n" + messagem,delete_after=300)
                if numdetect == 0:
                    pass
                else:
                    for dem in detective:
                        user = await self.client.fetch_user(dem)
                        await DMChannel.send(user,">>> **Mafia Game**\nYour role is The **Detective** :man_police_officer:\n\n**Your moves:**\n1. mafia invest eg.(mafia invest 1 //will investigate player 1)\n2. mafia skip       //Will skip tonight\nRemember to @ the bot before the commands",delete_after=1800)
                        await DMChannel.send(user,messagex,delete_after=300)
                if numdoc == 0:
                    pass
                else:
                    for dom in doctor:
                        user = await self.client.fetch_user(dom)
                        await DMChannel.send(user,">>> **Mafia Game**\nYour role is The **Doctor** :health_worker:\n\n**Your moves:**\n1. mafia heal eg.(mafia heal 1 //will heal player if a kill is attempted 1)\n2. mafia skip       //Will skip tonight\nRemember to @ the bot before the commands",delete_after=1800)
                        await DMChannel.send(user,messagex,delete_after=300)
                if not civilian:
                    pass
                else:
                    for civ in civilian:
                        user = await self.client.fetch_user(civ)
                        await DMChannel.send(user,">>> **Mafia Game**\nYour role is The **Civilian** :deaf_person:\nYou can't do shit at night",delete_after=1800)
                        await DMChannel.send(user,messagex,delete_after=300)
            else:
                await ctx.send(">>> You are not the host of this game", delete_after=10)
                return
        elif inputc == "skip":
            print(ctx.author.name+" Used mafia action")
            if timephase == 1:
                await ctx.send(">>> You cannot do this during the day", delete_after=10)
                return
            if not mafiacurrent:
                await ctx.send(">>> There is no Mafia games going on", delete_after=10)
                return
            if not mafiastart:
                await ctx.send(">>> There is Mafia Game no started", delete_after=10)
                return
            if not mafiaset:
                await ctx.send(">>> There is Mafia Game no set", delete_after=10)
                return
            if not ctx.author.id in aliveplayerid:
                await ctx.send(">>> Fk you understand", delete_after=10)
                return
            sender = ctx.author.id
            if sender in mafia:
                await ctx.send(">>> :detective:**Mafia**: You have skipped Night "+str(timenumber)+".", delete_after=30)
                mafiadone.append(sender)
                mafia.remove(sender)
            elif sender in detective:
                await ctx.send(">>> :man_police_officer:**Detective**: You have skipped Night "+str(timenumber)+".", delete_after=30)
                detectivedone.append(sender)
                detective.remove(sender)
            elif sender in doctor:
                await ctx.send(">>> :health_worker:**Doctor**: You have skipped Night "+str(timenumber)+".", delete_after=30)
                doctordone.append(sender)
                doctor.remove(sender)
            elif sender in civilian:
                await ctx.send(">>> :deaf_person:**Civilian**: You don't need to do anything at night :man_facepalming:", delete_after=30)
                return
            elif sender in pdead:
                await ctx.send(">>> :ghost:**Ghost**: You are dead you can't do anything now :man_facepalming:", delete_after=30)
                return
            else:
                await ctx.send(">>> You already used your move in Night "+str(timenumber)+".", delete_after=30)
                return
            totaltest = 3
            if not mafia:
                totaltest = totaltest - 1
            if not doctor:
                totaltest = totaltest - 1
            if not detective:
                totaltest = totaltest - 1
            if totaltest == 0:
                timenumber = timenumber + 1

        elif inputc == "kill":
            print(ctx.author.name+" Used mafia action")
            if timephase == 1:
                await ctx.send(">>> You cannot do this during the day", delete_after=10)
                return
            if not mafiacurrent:
                await ctx.send(">>> There is no Mafia games going on", delete_after=10)
                return
            if not mafiastart:
                await ctx.send(">>> There is Mafia Game no started", delete_after=10)
                return
            if not mafiaset:
                await ctx.send(">>> There is Mafia Game no set", delete_after=10)
                return
            if not ctx.author.id in aliveplayerid:
                await ctx.send(">>> Fk you understand", delete_after=10)
                return
            try:
                killinput = (int(input1)-1)
            except:
                await ctx.send(">>> Please only input numbers eg. (mafia kill 1) <- Player 1", delete_after=10)
                return
            if killinput >= len(aliveplayerid):
                await ctx.send(">>> Number out of range", delete_after=10)
                return
            sender = ctx.author.id
            if sender == aliveplayerid[killinput]:
                await ctx.send(">>> You can't target yourself", delete_after=10)
                return
            if sender in mafia:
                await ctx.send(">>> :detective:**Mafia**: You have chosen to **Kill** <@!"+str(aliveplayerid[killinput])+"> on Night "+str(timenumber)+".", delete_after=180)
                killlist.append(aliveplayerid[killinput])
                mafiadone.append(sender)
                mafia.remove(sender)
            elif sender in civilian:
                await ctx.send(">>> :deaf_person:**Civilian**: You don't need to do anything at night :man_facepalming:", delete_after=30)
                return
            elif sender in pdead:
                await ctx.send(">>> :ghost:**Ghost**: You are dead you can't do anything now :man_facepalming:", delete_after=30)
                return
            elif sender in detective:
                await ctx.send(">>> :man_police_officer:**Detective**: You can't kill people :man_shrugging:", delete_after=30)
                return
            elif sender in doctor:
                await ctx.send(">>> :health_worker:**Doctor**: WTF your a Doctor You can't kill people", delete_after=30)
                return
            else:
                await ctx.send(">>> You already used your move in Night "+str(timenumber)+".", delete_after=30)
                return
            totaltest = 3
            if not mafia:
                totaltest = totaltest - 1
            if not doctor:
                totaltest = totaltest - 1
            if not detective:
                totaltest = totaltest - 1
            if totaltest == 0:
                timenumber = timenumber + 1

        elif inputc == "invest":
            print(ctx.author.name+" Used mafia action")
            if timephase == 1:
                await ctx.send(">>> You cannot do this during the day", delete_after=10)
                return
            if not mafiacurrent:
                await ctx.send(">>> There is no Mafia games going on", delete_after=10)
                return
            if not mafiastart:
                await ctx.send(">>> There is Mafia Game no started", delete_after=10)
                return
            if not mafiaset:
                await ctx.send(">>> There is Mafia Game no set", delete_after=10)
                return
            if not ctx.author.id in aliveplayerid:
                await ctx.send(">>> Fk you understand", delete_after=10)
                return
            try:
                invinput = (int(input1)-1)
            except:
                await ctx.send(">>> Please only input numbers eg. (mafia invest 1) <- Player 1", delete_after=10)
                return
            if invinput >= len(aliveplayerid):
                await ctx.send(">>> Number out of range", delete_after=10)
                return
            sender = ctx.author.id
            if sender == aliveplayerid[invinput]:
                await ctx.send(">>> You can't target yourself", delete_after=10)
                return
            if sender in detective:
                await ctx.send(">>> :man_police_officer:**Detective**: You have chosen to **Investigate** <@!"+str(aliveplayerid[invinput])+"> on Night "+str(timenumber)+".", delete_after=180)
                investigate.append(str(sender)+"|"+str(aliveplayerid[invinput]))
                detectivedone.append(sender)
                detective.remove(sender)
            elif sender in mafia:
                await ctx.send(">>> :detective:**Mafia**: You can't Investigate people :man_shrugging:", delete_after=30)
                return
            elif sender in doctor:
                await ctx.send(">>> :health_worker:**Doctor**: You can't Investigate people", delete_after=30)
                return
            elif sender in civilian:
                await ctx.send(">>> :deaf_person:**Civilian**: You don't need to do anything at night :man_facepalming:", delete_after=30)
                return
            elif sender in pdead:
                await ctx.send(">>> :ghost:**Ghost**: You are dead you can't do anything now :man_facepalming:", delete_after=30)
                return
            else:
                await ctx.send(">>> You already used your move in Night "+str(timenumber)+".", delete_after=30)
                return
            totaltest = 3
            if not mafia:
                totaltest = totaltest - 1
            if not doctor:
                totaltest = totaltest - 1
            if not detective:
                totaltest = totaltest - 1
            if totaltest == 0:
                timenumber = timenumber + 1

        elif inputc == "heal":
            print(ctx.author.name+" Used mafia action")
            if timephase == 1:
                await ctx.send(">>> You cannot do this during the day", delete_after=10)
                return
            if not mafiacurrent:
                await ctx.send(">>> There is no Mafia games going on", delete_after=10)
                return
            if not mafiastart:
                await ctx.send(">>> There is Mafia Game no started", delete_after=10)
                return
            if not mafiaset:
                await ctx.send(">>> There is Mafia Game no set", delete_after=10)
                return
            if not ctx.author.id in aliveplayerid:
                await ctx.send(">>> Fk you understand", delete_after=10)
                return
            try:
                healinput = (int(input1)-1)
            except:
                await ctx.send(">>> Please only input numbers eg. (mafia invest 1) <- Player 1", delete_after=10)
                return
            if healinput >= len(aliveplayerid):
                await ctx.send(">>> Number out of range", delete_after=10)
                return
            sender = ctx.author.id
            if sender in doctor:
                await ctx.send(">>> :health_worker:**Doctor**: You have chosen to **Heal** <@!"+str(aliveplayerid[healinput])+"> on Night "+str(timenumber)+".", delete_after=180)
                heallist.append(aliveplayerid[healinput])
                doctordone.append(sender)
                doctor.remove(sender)
            elif sender in detective:
                await ctx.send(">>> :man_police_officer:**Detective**: You can't heal people", delete_after=30)
                return
            elif sender in mafia:
                await ctx.send(">>> :detective:**Mafia**: You can't Investigate people :man_shrugging:", delete_after=30)
                return
            elif sender in civilian:
                await ctx.send(">>> :deaf_person:**Civilian**: You don't need to do anything at night :man_facepalming:", delete_after=30)
                return
            elif sender in pdead:
                await ctx.send(">>> :ghost:**Ghost**: You are dead you can't do anything now :man_facepalming:", delete_after=30)
                return
            else:
                await ctx.send(">>> You already used your move in Night "+str(timenumber)+".", delete_after=30)
                return
            totaltest = 3
            if not mafia:
                totaltest = totaltest - 1
            if not doctor:
                totaltest = totaltest - 1
            if not detective:
                totaltest = totaltest - 1
            if totaltest == 0:
                timenumber = timenumber + 1

        if inputc == "vote":
            print(ctx.author.name+" Used mafia vote")
            if timephase == 0:
                await ctx.send(">>> You cannot do this during night", delete_after=10)
                return
            if not mafiacurrent:
                await ctx.send(">>> There is no Mafia games going on", delete_after=10)
                return
            if not mafiastart:
                await ctx.send(">>> There is Mafia Game no started", delete_after=10)
                return
            if not mafiaset:
                await ctx.send(">>> There is Mafia Game no set", delete_after=10)
                return
            if not ctx.author.id in aliveplayerid:
                await ctx.send(">>> Fk you understand", delete_after=10)
                return
            try:
                voteinput = int(input1)
            except:
                await ctx.send(">>> Please only input numbers eg. (mafia vote 0) <- 0 Skip", delete_after=10)
                return
            sender = ctx.author.id
            xvalue = len(aliveplayerid)
            if voteinput > xvalue:
                await ctx.send(">>> Fk you use your fking brain", delete_after=10)
                return
            if sender in voted:
                await ctx.send(">>> <@!"+str(sender)+"> You are not allowed to vote again", delete_after=30)
                return
            elif voteinput == 0:
                voted.append(sender)
                voting.append(0)
                await ctx.send(">>> <@!"+str(sender)+"> Has voted", delete_after=60)
                await ctx.message.delete()
                votingnumber = votingnumber - 1
                editvalue = xvalue - votingnumber
                await roommessage.edit(content="Number of Votes : "+str(editvalue)+"/"+str(xvalue),delete_after=600)
            else:
                voted.append(sender)
                voting.append(aliveplayerid[(voteinput-1)])
                await ctx.send(">>> <@!"+str(sender)+"> Has voted", delete_after=60)
                await ctx.message.delete()
                votingnumber = votingnumber - 1
                editvalue = xvalue - votingnumber
                await roommessage.edit(content="Number of Votes : "+str(editvalue)+"/"+str(xvalue),delete_after=600)

        if votingnumber == 0:
            voting2 = []
            votingnumber = 1
            voting = sorted(voting, key=voting.count, reverse=True)
            for votes in voting:
                if votes not in voting2:
                    voting2.append(votes)
            messagev = ":sunny: **Day "+str(timenumber)+" Voting** :sunny:\nVoting Results:"
            counting = 0
            checkcount = 0
            checktie = False
            for vote in voting2:
                counting = counting + 1
                x = voting.count(vote)
                if vote == 0:
                    messagev = messagev + "\n" + str(counting) + ". Skipped : "+str(x)
                else:
                    if checkcount == 0:
                        checkcount = x
                    elif checkcount == x:
                        checktie = True
                    messagev = messagev + "\n" + str(counting) + ". <@!"+str(vote)+"> : "+str(x)
            if voting[0] == 0:
                messagev = messagev + "\n\n Looks like Majority Skipped"
                await channeldef.send(messagev, delete_after=600)
                await asyncio.sleep(5)
            elif checktie:
                messagev = messagev + "\n\n Looks like it was a tie"
                await channeldef.send(messagev, delete_after=600)
                await asyncio.sleep(5)
            else:
                messagev = messagev + "\n\n <@!"+str(voting[0])+"> Was Hanged"
                if voting[0] in mafia:
                    messagev = messagev + "\nHe was a Mafia!"
                    mafia.remove(voting[0])
                elif voting[0] in detective:
                    messagev = messagev + "\nHe was a Detective!"
                    detective.remove(voting[0])
                elif voting[0] in doctor:
                    doctor = messagev + "\nHe was a Doctor!"
                    mafia.remove(voting[0])
                elif voting[0] in civilian:
                    messagev = messagev + "\nHe was a Civilian!"
                    civilian.remove(voting[0])
                aliveplayerid.remove(voting[0])
                pdead.append(voting[0])
                messagev = messagev + "\nYou have about 10 seconds to speak before the game continues"
                await channeldef.send(messagev, delete_after=600)
                await asyncio.sleep(10)
            timephase = 0
            voting = []
            if not mafia:
                endgame = True
            if len(mafia) == (len(aliveplayerid)-len(mafia)):
                endgame = True
            if not endgame:
                messagex = ">>> :crescent_moon: **Night "+str(timenumber)+" begins!** :crescent_moon:\n**Players Alive**:"
                counter = 0
                for ap in aliveplayerid:
                    counter = counter + 1
                    messagex = messagex + "\n" + str(counter) + ". <@!" + str(ap) + ">"
                await channeldef.send(messagex, delete_after=600)

                for mm in mafia:
                    user = await self.client.fetch_user(mm)
                    await DMChannel.send(user, messagex + "\n" + messagem, delete_after=300)
                if numdetect == 0:
                    pass
                else:
                    for dem in detective:
                        user = await self.client.fetch_user(dem)
                        await DMChannel.send(user, messagex, delete_after=300)
                if numdoc == 0:
                    pass
                else:
                    for dom in doctor:
                        user = await self.client.fetch_user(dom)
                        await DMChannel.send(user, messagex, delete_after=300)
                if not civilian:
                    pass
                else:
                    for civ in civilian:
                        user = await self.client.fetch_user(civ)
                        await DMChannel.send(user, messagex, delete_after=300)

        if timenumber > timenumber2:
            timenumber2 = timenumber
            timephase = 1
            mafia = mafiadone[:]
            detective = detectivedone[:]
            doctor = doctordone[:]
            mafiadone = []
            doctordone = []
            detectivedone = []
            civiliandone = []
            killremove = []
            daymessage = ":sunny: **Day "+str(timenumber)+" begins** :sunny:"
            if not heallist:
                pass
            else:
                for heal in heallist:
                    if heal in killlist:
                        daymessage = daymessage + "\nA Mafia member attempted to **Murder** <@!"+str(heal)+"> but he/she was saved by a **Doctor**."
                        killremove.append(heal)
            if not investigate:
                pass
            else:
                for invs in investigate:
                    try:
                        invsplit = invs.split("|")
                        detec = int(invsplit[0])
                        target = int(invsplit[1])
                        user = await self.client.fetch_user(detec)
                        if target in mafia:
                            await DMChannel.send(user,">>> **Mafia Game**\n:man_police_officer:**Detective**: <@!"+str(target)+"> Was found to have ties with the Mafia",delete_after=180)
                        elif target in doctor:
                            await DMChannel.send(user,">>> **Mafia Game**\n:man_police_officer:**Detective**: <@!"+str(target)+"> Was found to be a Medical Professional",delete_after=180)
                        elif target in detective:
                            await DMChannel.send(user,">>> **Mafia Game**\n:man_police_officer:**Detective**: <@!"+str(target)+"> Was found to be an Private Eye",delete_after=180)
                        elif target in civilian:
                            await DMChannel.send(user,">>> **Mafia Game**\n:man_police_officer:**Detective**: <@!"+str(target)+"> Was found to be a Civilian",delete_after=180)
                    except:
                        pass
            if not killremove:
                pass
            else:
                for removing in killremove:
                    killlist.remove(removing)
            if not killlist:
                daymessage = daymessage + "\n\n**No Deaths Today.**"
            else:
                for kills in killlist:
                    daymessage = daymessage + "\n<@!" + str(kills) + ">" + random.choice(randokilllines)
                    pdead.append(kills)
                    aliveplayerid.remove(kills)
                    if kills in mafia:
                        mafia.remove(kills)
                    elif kills in detective:
                        detective.remove(kills)
                    elif kills in doctor:
                        mafia.remove(kills)
                    elif kills in civilian:
                        civilian.remove(kills)
            daymessage = daymessage + "\n\nDead Players:"
            if not pdead:
                pass
            else:
                for deadp in pdead:
                    daymessage = daymessage + " <@!" + str(deadp) + ">,"
            heallist = []
            killlist = []
            investigate = []
            if not mafia:
                endgame = True
            if len(mafia) == (len(aliveplayerid)-len(mafia)):
                endgame = True
            if not endgame:
                daymessage = daymessage + "\n\nThe time has come to vote to find the **Mafia**\nUse mafia vote  eg.(mafia vote 0) to skip //You can type votes in the main chat\nPlayers Alive:"
                counter = 0
                roommessage = ''
                for aplayer in aliveplayerid:
                    counter = counter + 1
                    daymessage = daymessage + "\n"+str(counter)+". <@!"+str(aplayer)+">"
                await channeldef.send(daymessage, delete_after=1800)
                votingnumber = len(aliveplayerid)
                roommessage = await channeldef.send("Number of Votes : 0/"+str(votingnumber),delete_after=600)
                voted = []

        if endgame:
            endgame = False
            messagee = ">>> **Mafia Game** Has Ended!"
            if len(mafia) == 0:
                messagee = messagee + "\n:medal:The Civilians Won!:medal:"
            else:
                messagee = messagee + "\n:medal:The Mafia Won!:medal:"
            await channeldef.send(messagee, delete_after=1800)
            mafiacurrent = False
            mafiastart = False
            mafiaset = False
            endgame = False
            joinedplayer = []
            joinedplayerid = []
            aliveplayerid = []
            investigate = []
            killlist = []
            heallist = []
            mafia = []
            nummafia = 0
            civilian = []
            mafiadone = []
            voted = []
            doctordone = []
            detectivedone = []
            civiliandone = []
            voting = []
            voting2 = []
            votingnumber = 0
            messagem = ''
            doctor = []
            numdoc = 0
            timenumber = 0
            timenumber2 = 0
            detective = []
            numdetect = 0
            pdead = []
            roommessage = ''
            channeldef = ''
            hostid = ''
            timephase = 0
            await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Music"))

        await asyncio.sleep(3)
        await ctx.message.delete()


def setup(client):
    client.add_cog(Mafia(client))
