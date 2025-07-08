import discord
import aiohttp
from discord.ext import commands
from discord.ext.commands import BucketType
import os
import dotenv
# Charger les variables d'environnement
dotenv.load_dotenv()

class Valorant(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name="valorantstats", description="Affiche les stats Valorant d’un joueur")
    @commands.cooldown(rate=1, per=30, type=BucketType.guild)  # cooldown serveur
    async def valorantstats(self, ctx, pseudo: str):
        await ctx.defer()

        if "#" not in pseudo:
            await ctx.send("Merci d'utiliser le format `Pseudo#TAG`.")
            return

        name, tag = pseudo.split("#")
        region = "eu"

        headers = {
            "Authorization": os.getenv("HENRIK_API_KEY")
        }

        async with aiohttp.ClientSession() as session:
            url_account = f"https://api.henrikdev.xyz/valorant/v1/account/{name}/{tag}"
            url_mmr = f"https://api.henrikdev.xyz/valorant/v1/mmr/{region}/{name}/{tag}"

            async with session.get(url_account, headers=headers) as resp:
                account = await resp.json()

            async with session.get(url_mmr, headers=headers) as resp:
                mmr = await resp.json()

        if account.get("status") != 200:
            await ctx.send("Compte introuvable ou inaccessible.")
            return
        if mmr.get("status") != 200:
            await ctx.send("Impossible de récupérer les stats MMR.")
            return

        acc_data = account["data"]
        mmr_data = mmr["data"]

        embed = discord.Embed(
            title=f"📊 Stats de {acc_data['name']}#{acc_data['tag']}",
            color=discord.Color.from_rgb(240, 240, 240)  # Couleur très claire
        )
        embed.set_thumbnail(url=acc_data["card"]["small"])
        embed.add_field(name="🎖️ Niveau", value=acc_data.get("account_level", "N/A"), inline=True)
        embed.add_field(name="📈 Rang actuel", value=mmr_data.get("currenttierpatched", "Inconnu"), inline=True)
        embed.add_field(name="🔢 Rang du passe", value=mmr_data.get("ranking_in_tier", "N/A"), inline=True)
        embed.add_field(name="💡 ELO estimé", value=mmr_data.get("elo", "N/A"), inline=True)
        embed.add_field(name="🔄 MMR dernière game", value=mmr_data.get("mmr_change_to_last_game", "N/A"), inline=True)
        embed.add_field(name="🌍 Région", value=acc_data.get("region", "N/A").upper(), inline=True)
        embed.add_field(name="🕒 Dernière MAJ", value=acc_data.get("last_update", "N/A"), inline=True)
        embed.set_footer(text="Données fournies par api.henrikdev.xyz")

        await ctx.send(embed=embed)

    @valorantstats.error
    async def valorantstats_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"⏳ Cette commande est en cooldown. Réessaie dans {int(error.retry_after)} secondes.", ephemeral=True)
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Merci de fournir un pseudo au format `Pseudo#TAG`.")
        else:
            await ctx.send("Une erreur est survenue.")

async def setup(bot):
    await bot.add_cog(Valorant(bot))