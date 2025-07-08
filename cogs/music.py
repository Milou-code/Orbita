import discord
try:
    import discord.opus
    discord.opus.load_opus("/opt/homebrew/lib/libopus.dylib")  # Mac par défaut
except Exception:
    try:
        import discord.opus
        discord.opus.load_opus("/usr/lib/arm-linux-gnueabihf/libopus.so.0")  # Raspberry Pi
    except Exception:
        pass  # Ignore si la lib n'est pas trouvée, Discord affichera une erreur explicite
from discord.ext import commands
from discord import FFmpegPCMAudio
import yt_dlp

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.voice_clients = {}

    @commands.command()
    async def play(self, ctx, *, query: str):
        if ctx.author.voice is None:
            await ctx.send("Vous devez être dans un salon vocal.")
            return

        channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await channel.connect()
        elif ctx.voice_client.channel != channel:
            await ctx.voice_client.move_to(channel)

        ctx.voice_client.stop()

        # Recherche et extraction du flux audio avec yt-dlp
        ydl_opts = {
            'format': 'bestaudio/best',
            'noplaylist': True,
            'quiet': True,
            'default_search': 'ytsearch',
            'extract_flat': False,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(query, download=False)
            if 'entries' in info:
                info = info['entries'][0]
            url2 = info['url']
            title = info.get('title', query)

        source = FFmpegPCMAudio(url2)
        ctx.voice_client.play(source, after=lambda e: print(f'Erreur: {e}') if e else None)
        await ctx.send(f"Lecture de la musique : {title}")

    @commands.command()
    async def pause(self, ctx):
        if ctx.voice_client and ctx.voice_client.is_playing():
            ctx.voice_client.pause()
            await ctx.send("Musique en pause.")
        else:
            await ctx.send("Aucune musique en cours de lecture.")

    @commands.command()
    async def resume(self, ctx):
        if ctx.voice_client and ctx.voice_client.is_paused():
            ctx.voice_client.resume()
            await ctx.send("Reprise de la musique.")
        else:
            await ctx.send("Aucune musique en pause.")

async def setup(bot):
    await bot.add_cog(Music(bot))