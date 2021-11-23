import discord
from discord.ext import commands
import youtube_dl

class music(commands.Cog):
  def __init__(self, client):
    self.client = client
    
    
  @commands.command()
  async def disconnect(self,ctx):
    await ctx.voice_client.disconnect()
    await ctx.channel.send('')


  @commands.command(brief = "Playing music from YouTube")
  async def p(self,ctx,url):
    voice_channel = ctx.author.voice.channel
    if ctx.voice_client is None:
      await voice_channel.connect()
      await ctx.channel.send('```boss of this gym is going to play the song ASS he can!\n♂ lets go ♂```')
    else:
      await ctx.voice_client.move_to(voice_channel)    
    ctx.voice_client.stop()
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    YDL_OPTIONS = {'format':"bestaudio"}
    vc = ctx.voice_client

    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
      info = ydl.extract_info(url, download=False)
      url2 = info['formats'] [0] ['url']
      source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
      vc.play(source)
      

  @commands.command(brief="Pauses the currently playing song.")
  async def pause(self, ctx):
        # Checks if music is playing and pauses it, otherwise sends the player a message that nothing is playing
    try:
      ctx.voice_client.pause()
    except:
      await ctx.send(f"{ctx.author.mention} i'm not playing music at the moment!")


  @commands.command(brief="Resumes the paused song.")
  async def resume(self, ctx):
        # Checks if music is paused and resumes it, otherwise sends the player a message that nothing is playing
      ctx.voice_client.resume()
      await music.get_channel("896535628613836840").send("bot is online")


def setup(client):
    client.add_cog(music(client))