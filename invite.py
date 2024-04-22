import discord
import datetime
import botconfig
from discord.commands import OptionChoice, slash_command, option
from discord.ext import commands
from discord.ui import View
import ciscord
class einladen(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


        print(f"{ciscord.einladen_py}")


    @slash_command(name="einladen", description="Möchtest du NoraBot einladen?")
    @option(name="funktion", description="Server, Bot", required=False)
    async def einladen(self, ctx, funktion):
        Befehl = "/einladen"
        if funktion == "Bot":
            embed = discord.Embed(color=0x00BFFF)
            embed.set_thumbnail(url=str(ctx.author.display_avatar.url))
            embed.timestamp = datetime.datetime.now()
            embed.add_field(name="NoraBot Offiziell",
                            value="https://discord.com/api/oauth2/authorize?client_id=1191775455305539604&permissions=1789323979862&scope=bot",
                            inline=False)
            embed.add_field(name="NoraBot BETA",
                            value="**Dieser Link wurde noch nicht Bereit gestellt!**")
            embed.set_footer(text=f"{botconfig.Botname} • {Befehl} • {botconfig.Version}")
            await ctx.respond(embed=embed)
            return

        if funktion == "bot":
            embed = discord.Embed(color=0x00BFFF)
            embed.set_thumbnail(url=str(ctx.author.display_avatar.url))
            embed.timestamp = datetime.datetime.now()
            embed.add_field(name="NoraBot Offiziell",
                            value="https://discord.com/api/oauth2/authorize?client_id=1191775455305539604&permissions=1789323979862&scope=bot",
                            inline=False)
            embed.add_field(name="NoraBot BETA",
                            value="**Dieser Link wurde noch nicht Bereit gestellt!**")
            embed.set_footer(text=f"{botconfig.Botname} • {Befehl} • {botconfig.Version}")
            await ctx.respond(embed=embed)
            return

        if funktion == "Server":
            embed = discord.Embed(color=0x00BFFF)
            embed.set_thumbnail(url=str(ctx.author.display_avatar.url))
            embed.timestamp = datetime.datetime.now()
            embed.add_field(name="Server Einladung:",
                            value="https://discord.gg/CqsA9Ke9zP",
                            inline=False)
            embed.set_footer(text=f"{botconfig.Botname} • {Befehl} • {botconfig.Version}")
            await ctx.respond(embed=embed)
            return

        if funktion == "server":
            embed = discord.Embed(color=0x00BFFF)
            embed.set_thumbnail(url=str(ctx.author.display_avatar.url))
            embed.timestamp = datetime.datetime.now()
            embed.add_field(name="Server Einladung:",
                            value="https://discord.gg/CqsA9Ke9zP",
                            inline=False)
            embed.set_footer(text=f"{botconfig.Botname} • {Befehl} • {botconfig.Version}")
            await ctx.respond(embed=embed)
            return

        else:
            embed = discord.Embed(color=0xff0000)
            embed.set_thumbnail(url=str(ctx.author.display_avatar.url))
            embed.timestamp = datetime.datetime.now()
            embed.add_field(name="Ein Fehler ist aufgetreten! - 404",
                            value="Du musst bei ``funktion`` eine auswahl treffen! \n Server • Bot", inline=False)
            embed.set_footer(text=f"{botconfig.Botname} • {Befehl} • {botconfig.Version}")
            await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(einladen(bot))