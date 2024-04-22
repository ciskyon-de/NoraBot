import discord
import datetime
import botconfig
from discord.commands import OptionChoice, slash_command, option
from discord.ext import commands
from discord.ui import View
import ciscord

class botinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @slash_command(name="botinfo", description="Finde mehr über NoraBot raus!")

    async def info(self, ctx):

            embed = discord.Embed(color=ciscord.farbe_orange)
            embed.add_field(name=f"Hier siehst du ein paar Statistiken von NoraBot, die in speziellen Fällen nützlich sein können.",
                            value="", inline=False)
            embed.add_field(name="**Entwickler**",
                            value="``norigenora``", inline=False)
            embed.add_field(name="**Hier siehst du ein paar spannende Infos**",
                            value=f"Online seit: ``{ciscord.Startzeit.strftime(botconfig.botinfo_date_format)}``\nAktuelle Version:``1.0.0``\nAktiv auf: ``{str(len(self.bot.guilds))} Server.``\nAkutelle Reichweite: ``{str(len(self.bot.users))} Mitglieder.``\nOffene Tickets: ``0 Tickets``", inline=False)
            embed.add_field(name="**Angepinnt**",
                            value=f"Bot Sprache ist ``Python.``\nNoraBot [HIER](https://discord.com/oauth2/authorize?client_id=1227547163265863680) einladen!\nUnsere Dokumentation ist noch in Arbeit!")
            embed.set_thumbnail(url=str(ctx.author.display_avatar.url))
            await ctx.respond(embed=embed)
            return


def setup(bot):
    bot.add_cog(botinfo(bot))

