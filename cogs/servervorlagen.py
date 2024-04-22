import discord
import datetime
import botconfig
from discord.commands import OptionChoice, slash_command, option
from discord.ext import commands
from discord.ui import View

class servervorlage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    Befehl = "/servervorlagen"
    @slash_command(name="servervorlagen", description="Hier sind angefertigte Servervorlagen von NoraBot!")

    async def servervorlagen(self, ctx):

            embed = discord.Embed(color=0xFfff00)
            embed.set_thumbnail(url=str(ctx.author.display_avatar.url))
            embed.timestamp = datetime.datetime.now()
            embed.add_field(name=f"SERVERVORLAGEN | STAND: 04.01.2024",
                            value="<:warn:1191905803230261268> Aktuell gibt es noch keine Vorlagen in der Liste!",
                            inline=False)
            embed.set_footer(text=f"{botconfig.Botname} • /servervorlagen • {botconfig.Version}")
            await ctx.respond(embed=embed)
            return



def setup(bot):
    bot.add_cog(servervorlage(bot))