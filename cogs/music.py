# By robotic-nation
import discord
from discord.ext import commands
import youtube_dl
import os
import ffmpeg
import asyncio

checkconnect = False

class Music(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def music(self, ctx, *args):
        global checkconnect
        inputc = ''
        input1 = ''
        try:
            inputc = args[0].lower()
            input1 = args[1]
        except:
            pass

        if inputc == 'help':
            print(ctx.author.name+" Used music help")
            await ctx.send(">>> **Music Commands**\nmusic help\nmusic play\nmusic stop\nmusic pause\nmusic resume\nmusic leave", delete_after=30)

        if inputc == 'play':
            print(ctx.author.name+" Used music play")
            if 'www.youtube.com/watch?v=' not in str(input1):
                await ctx.send(">>> Video must be an url from youtube", delete_after=10)
                return
            try:
                voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
                voice.stop()
                await asyncio.sleep(1)
                voice.stop()
            except:
                pass
            song_there = os.path.isfile("song.mp3")
            try:
                if song_there:
                    os.remove("song.mp3")
            except PermissionError:
                await ctx.send("Wait for the current playing music to end or use the 'stop' command", delete_after=10)
                return
            channel1 = ctx.author.voice.channel
            if not checkconnect:
                checkconnect = True
                await channel1.connect()
            voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)

            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }

            sIDx = input1.split('v=')
            sID = str(sIDx[1])
            downloadt = True
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                dictMeta = ydl.extract_info(
                    "https://www.youtube.com/watch?v={sID}".format(sID=sID),
                    download=False)
                if int(dictMeta['duration']) > 600:
                    downloadt = False
                if downloadt:
                    ydl.download([input1])
            if downloadt:
                for file in os.listdir("./"):
                    if file.endswith(".mp3"):
                        os.rename(file, "song.mp3")
                voice.play(discord.FFmpegPCMAudio("song.mp3"))
            else:
                await ctx.send('Video is more than 10 mins cannot be played', delete_after=10)

        if inputc == 'leave':
            print(ctx.author.name+" Used music leave")
            voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
            if voice.is_connected():
                checkconnect = False
                await voice.disconnect()
            else:
                await ctx.send("The bot is not connected to a voice channel.", delete_after=10)

        if inputc == 'pause':
            print(ctx.author.name+" Used music pause")
            voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
            if voice.is_playing():
                voice.pause()
            else:
                await ctx.send("Currently no audio is playing.", delete_after=10)

        if inputc == 'resume':
            print(ctx.author.name+" Used music resume")
            voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
            if voice.is_paused():
                voice.resume()
            else:
                await ctx.send("The audio is not paused.", delete_after=10)

        if inputc == 'stop':
            print(ctx.author.name+" Used music stop")
            voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
            voice.stop()
        await asyncio.sleep(10.5)
        await ctx.message.delete()


def setup(client):
    client.add_cog(Music(client))

# If you wish to securely hide your token, you can do so in a .env file.
# 1. Create a .env in the same directory as your Python scripts
# 2. In the .env file format your variables like this: VARIABLE_NAME=your_token_here
# 3. At the top of the Python script, import os
# 4. In Python, you can read a .env file using this syntax:
# token = os.getenv(VARIABLE_NAME)
