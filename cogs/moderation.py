from discord.ext import commands
import discord

class ModerationCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

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

async def setup(bot):
    await bot.add_cog(ModerationCog(bot))