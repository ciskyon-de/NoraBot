import discord
import botconfig
import ciscord
from discord.commands import OptionChoice, slash_command, option
from discord.ext import commands


class einladen(commands.Cog):
    def __int__(self, bot):
        self.bot = bot
    @slash_command(name="einladen", description="Lade NoraBot auf dein Server ein!")

    async def invite(self, ctx):

            embed = discord.Embed(color=ciscord.farbe_orange)
            embed.add_field(name="NoraBot Einladen!",
                            value="[JETZT EINLADEN!](https://discord.com/oauth2/authorize?client_id=1227547163265863680)", inline=False)
            embed.set_thumbnail(url=str(ctx.author.display_avatar.url))
            await ctx.respond(embed=embed)
            return

def setup(bot):
    bot.add_cog(einladen(bot))
