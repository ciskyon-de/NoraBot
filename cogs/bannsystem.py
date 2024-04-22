import discord
import datetime

from discord.ext.commands import Context
from discord.ext.commands.converter import T_co

import botconfig
from discord.commands import OptionChoice, SlashCommandGroup, option
from discord.ext import commands
from discord.ui import View
import aiosqlite

class IDConverter(commands.Converter):
    async def convert(self, ctx, argument):
        try:
            user_id = int(argument.strip('<@!>'))
            if user_id > 0:
                return user_id
            else:
                raise commands.BadArgument("Ungültige Discord-ID.")
        except ValueError:
            raise commands.BadArgument(
                "Ungültige Benutzer-ID. Bitte verwende eine gültige Benutzer-ID in der Form <@Benutzer-ID>.")

class bannsystem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listeners()
    async def on_ready(self):
        async with aiosqlite.connect('norabot_bannsystem.db') as nora:
            await nora.execute('''
                CREATE TABLE IF NOT EXISITS users (
                    user_id INTEGER PRIMARY KEY,
                    reason TEXT
                )
            ''')
            await nora.execute('''
                CREATE TABLE IF NOT EXISTS servers (
                    server_id INTEGER PRIMARY KEY,
                    reason TEXT
                )
            ''')
            await nora.commit()

    globalbann = SlashCommandGroup(name="globalbann", description="Verwalte die Global-Bannlisten für User und Server.",
                                   guild_ids=[1191891302187544701, 1104557165391384586],
                                   has_role=[1192488852921798747, 1192568206271975595, 1116484318487924756,
                                             1111338391594864690])
    ban = globalbann.create_subgroup(name="ban", description="Verwalte die Mitgliedern in der Bannliste")
    unban = globalbann.create_subgroup(name="unban", description="Verwalte die Servern in der Bannliste")

    @ban.command(name="user", description="Füge Jemanden in der Bannliste hinzu.")
    @option(name="mitglied", description="Welche Person soll ich ignorieren?")
    @option(name="grund", description="Und warum du?")
    async def add_user(selfself, ctx, mitglied: discord.Member, grund):
        Befehl = "/globalbann ban user"
        Befehlext = f"/globalbann ban user mitglied: {mitglied.name} ({mitglied.id}), grund: {grund}"



def setup(bot):
    bot.add_cog(bannsystem(bot))