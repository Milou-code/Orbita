from discord.ext import commands
import discord

class BaseCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(hidden=True)
    async def hello(self, ctx):
        await ctx.reply("Hello world ! Mon nom est Orbita.")

    @commands.hybrid_command(nom="decompte", description="Fait un décompte jusqu'au top départ.")
    async def decompte(self, ctx, nombre: int):
        if nombre < 1:
            await ctx.reply("Le nombre doit être supérieur à 0.")
        else:
            await ctx.send(f"Départ dans ...")
            for i in range(nombre, 0, -1):
                await ctx.send(i)
            await ctx.send("GO !")

    @commands.hybrid_command(nom="repeter", description="Répète le message donné.")
    async def repeter(self, ctx, *, message: str):
        if len(message) > 2000:
            await ctx.reply("Le message est trop long !")
        else:
            await ctx.send(message)

    @commands.hybrid_command(nom="ping", description="Renvoie la latence du bot.")
    async def ping(self, ctx):
        latency = round(self.bot.latency * 1000)
        await ctx.reply(f"Pong ! Latence : {latency} ms")

async def setup(bot):
    await bot.add_cog(BaseCog(bot))