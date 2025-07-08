import discord
from dotenv import load_dotenv
import os
from discord.ext import commands

load_dotenv()

class Orbita(commands.Bot):
    async def setup_hook(self):
        # Chargement des cogs
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                await self.load_extension(f"cogs.{filename[:-3]}")
                print(f"Cog {filename[:-3]} chargé.")
                
print("Lancement du bot...")
bot = Orbita(command_prefix="+", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"Bot allumé !")
    # Synchronisation des commandes slash
    print("Synchronisation des commandes slashs ...")
    try:
        synced = await bot.tree.sync()
        print(f"Commandes synchronisées : {len(synced)}")
    except Exception as e:
        print(f"Erreur lors de la synchronisation des commandes : {e}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    else:
        if message.content.lower().startswith("bonjour") or message.content.lower().startswith("salut"):
            await message.channel.send(f"Bonjour {message.author.mention} ! Je suis **Orbita**, comment vas-tu ?")

bot.run(os.getenv("DISCORD_TOKEN"))