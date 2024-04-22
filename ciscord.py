import datetime
import botconfig
import discord
import os
from dotenv import load_dotenv
from discord.ext import tasks, commands
import asyncio
import main



# ----------------------------------------
# -- Informationen zur Mod!
# ----------------------------------------

Modname = "Erweiterung: Ciscord"
Version = "Version: 2.10.1"
Inhaber = "Inhaber: norigenora"
Lastupdate = "Last Update: 09.02.2024"
abstand = "-------------------------------------"

# ----------------------------------------
# -- Alle Log Sachen!
# ----------------------------------------

Botname = "NoraBot"
Botversion = "Ver: NoraBot - 1.0.0"
Log = 1228052824311464056
Devs = "norigenora & clarigeclara"
Support = "NoraBot Support - 1191891302187544701"
main_py = "main.py wurde Erfolgreich geladen!"
heiii_py = "heiii.py wurde Erfolgreich geladen!"
botinfo_py = "botinfo.py wurde Erfolgreich geladen!"
einladen_py = "invite.py wurde Erfolgreich geladen!"
bannsystem_py = "bannsystem.py wurde Erfolgreich geladen!"
ausschalten_py = "ausschalten.py wurde Erfolgreich geladen!"
cd_py = "ciscord.py wurde Erfolgreich geladen!"
online = "Ich bin nun Online!"

# -----------------------------------------
# -- Alle Farbcodes!
# -----------------------------------------

farbe_grun = 0x7CFC00
farbe_blau = 0x4876FF
farbe_orange = 0xFFA500
farbe_lila = 0xE066FF
farbe_pink = 0xff00ff
farbe_weiss = 0xFFFFFF
farbe_schwarz = 0x000000
farbe_gelb = 0xffd700
farbe_rot = 0xff0000
farbe_cyan = 0x00ffff

# ------------------------------------------
# -- Willkommen System IDs!
# ------------------------------------------

Wlc_ServerID1 = 1231729975963553812
Wlc_ChannelID1 = 1231729976668323876
Wlc_BotID1 = 1227547163265863680

# ------------------------------------------
# -- Footer Texte!
# ------------------------------------------

Footer_botinfo = f"NoraBot - /botinfo - {datetime}"
Footer_einladen = f"NoraBot - /einladen - {datetime}"
Footer_bannsystem = f"NoraBot - /bannsystem - {datetime}"
Footer_dashboard = f"NoraBot - /dashboard - {datetime}"
Footer_witz = f"NoraBot - /witz - {datetime}"
Footer_hausverbot = f"NoraBot - /hausverbot - {datetime}"
Footer_rauswerfen = f"NoraBot - /rauswerfen - {datetime}"

# -------------------------------------------
# -- Fehlercodes Embed!
# -------------------------------------------

Fehler_botinfo = "Der Befehl ``/botinfo`` ist leider nicht Verfügbar oder Defekt! Geben sie ``/dashboard`` ein um den Befehls Status zu sehen!"
Fehler_bannsystem = "Der Befehl ``/bannsystem`` konnte nicht Erfolgreich beendet werden! Es liegt vielleicht daran das du keine Berechtigung hast. Geben sie ``/dashboard`` ein um den Befehls Status zu sehen!"
Fehler_einladen = "Huh... Dies ist komisch! Es kann nur daran liegen das die folgende Anwendung einen Fehler hat! Melden sie sich im Support."

# -------------------------------------------
# -- Alle Witze!
# -------------------------------------------

# COMMING SOON!

# -------------------------------------------
# -- Wichtige Links!
# -------------------------------------------

Service_Botlink = "https://discord.com/api/oauth2/authorize?client_id=1191775455305539604&permissions=19407816779798&scope=bot"
Service_serverlink = "https://discord.gg/AsAt6cC9PP"

# -------------------------------------------
# -- Bot Befehle laden!
# -------------------------------------------

Load_bot = "NoraBot"
Load_botinfo = "cogs.botinfo"
Load_willkommen = "cogs.willkommen"
Load_bannsystem = "cogs.bannsystem"
Load_einladen = "cogs.einladen"
Load_ciscord = "cogs.ciscord"
Load_welcome = "cogs.welcome"

# -------------------------------------------
# -- Bot Status!
# -------------------------------------------


Status1 = "Hilfe mit /hilfe"
Status2 = "Version: 1.0.0"


# -------------------------------------------

class load(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

print(f"{abstand}")
print(f"{cd_py}")


def setup(bot):
    bot.add_cog(load(bot))


# -------------------------------------------


Startzeit = datetime.datetime.now()
