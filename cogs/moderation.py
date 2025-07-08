import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = discord.Color.from_rgb(240, 240, 240)  # Couleur très claire

    @commands.hybrid_command(hidden=True)
    async def warn(self, ctx, member: discord.Member, *, reason: str = "Aucune raison fournie."):
        if ctx.author.guild_permissions.manage_messages:
            await ctx.send(f"{member.mention} a été averti pour : {reason} par {ctx.author.mention}")
    
    @commands.hybrid_command(hidden=True)
    async def kick(self, ctx, member: discord.Member, *, reason: str = "Aucune raison fournie."):
        if ctx.author.guild_permissions.kick_members:
            try:
                await member.send(f"Vous avez été **expulsé** du serveur : **{ctx.guild.name}** pour : *{reason}*")
            except Exception:
                pass  # Ignore si le MP ne peut pas être envoyé
            await member.kick(reason=reason)
            await ctx.send(f"{member.mention} a été expulsé pour : {reason} par {ctx.author.mention}")

    @commands.hybrid_command(hidden=True)
    async def ban(self, ctx, member: discord.Member, *, reason: str = "Aucune raison fournie."):
        if ctx.author.guild_permissions.ban_members:
            try:
                await member.send(f"Vous avez été **banni** du serveur : **{ctx.guild.name}** pour : *{reason}*")
            except Exception:
                pass
            await member.ban(reason=reason)
            await ctx.send(f"{member.mention} a été banni pour : {reason} par {ctx.author.mention}")

    @commands.hybrid_command(name="postregelement", description="Envoie le règlement du serveur dans le salon.")
    @commands.has_permissions(administrator=True)
    async def postregelement(self, ctx):
        embed = discord.Embed(
            title=":closed_book: - Règlement du Serveur des Roulias",
            description=(
                "Tous bon roulia se doit de respecter ces règles.\n\n"
                "**1. Respect avant tout**\n"
                "> Soyez respectueux envers tous les membres.\n"
                "> Aucune forme d’insulte, de discrimination, d’harcèlement ou de comportement toxique ne sera tolérée.\n\n"
                "**2. Pas de spoil sauvage**\n"
                "> Que ce soit pour un match, un jeu ou une série/film, utilisez les balises spoiler (||comme ceci||) pour préserver l'expérience des autres.\n\n"
                "**3. Contenu approprié uniquement**\n"
                "> Partagez uniquement des contenus liés aux thématiques du serveur.\n"
                "> Aucun contenu NSFW, choquant ou illégal ne sera toléré.\n"
                "> Les liens vers des sites illégaux ou non autorisés sont strictement interdits.\n\n"
                "**4. Pas de spam**\n"
                "> Évitez le flood, les messages en boucle, l’abus de majuscules ou d’emojis.\n\n"
                "**5. Pas de pub sans autorisation**\n"
                "> Il est interdit de faire de la promotion pour d'autres serveurs Discord, chaînes, sites ou produits sans l'accord du staff.\n"
                "> Les liens de streaming ou de paris sont tolérés uniquement dans les salons prévus à cet effet et selon les règles de Discord.\n\n"
                ":warning: *En cas de non-respect du règlement, des sanctions pourront être appliquées : avertissement, mute, kick, ban définitif selon la gravité de l’infraction.*\n\n"
                "**Merci de contribuer à une communauté *saine* et *agréable* !**"
            ),
            color=self.color
        )
        embed.set_footer(text="Le Staff des Roulias")
        await ctx.send(embed=embed)
        try:
            await ctx.message.delete()
        except Exception:
            pass

    @commands.hybrid_command(name="postreseaux", description="Envoie les liens des réseaux sociaux dans le salon.")
    @commands.has_permissions(administrator=True)
    async def postreseaux(self, ctx):
        embed = discord.Embed(
            title=":mobile_phone:・**Retrouve-moi sur les réseaux !**",
            description=(
                "─────────────────────────────\n"
                "Envie de suivre mes actus, mes projets ou tout simplement me soutenir ?\n"
                "Voici tous mes liens officiels :point_down:\n\n"
                ":star2: **Twitch** → [twitch.tv/monpseudo](https://twitch.tv/theroyalebros)\n"
                ":speech_balloon: **TikTok** → [tiktok.com/@monpseudo](https://tiktok.com/@theroyalebros)\n\n"
                ":dart: N’hésite pas à t’abonner, liker, partager ou venir discuter avec moi sur les lives !"
            ),
            color=self.color
        )
        embed.set_footer(text="Merci pour ton soutien !")
        await ctx.send(embed=embed)
        try:
            await ctx.message.delete()
        except Exception:
            pass

    @commands.hybrid_command(name="clear", description="Supprime un certain nombre de messages dans le salon.")
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, nombre: int):
        if nombre < 1 or nombre > 100:
            await ctx.send("Le nombre de messages à supprimer doit être compris entre 1 et 100.")
            return

        deleted = await ctx.channel.purge(limit=nombre + 1)
        await ctx.send(f"J'ai **supprimé** {len(deleted) - 1} messages.", delete_after=5)

async def setup(bot):
    await bot.add_cog(Moderation(bot))