import discord
import datetime
from discord.commands import OptionChoice, slash_command, option
from discord.ext import commands
from discord.ui import View
import ciscord



class befehle(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(befehle(bot))