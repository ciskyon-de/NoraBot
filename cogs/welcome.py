import discord
from discord.ext import commands

import ciscord


class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        print(f'Ich wurde in den Server "{guild.name}" eingeladen.')
        channel = discord.utils.get(guild.text_channels)
        if channel is not None:
            embed = discord.Embed(title="NoraBot wurde Eingeladen!",
                                  description="",
                                  color=ciscord.farbe_orange)
            embed.add_field(name="**Unsere Links**",
                            value="[DISCORD](https://discord.gg/BY2Mp6t6Gq)\n[STATUS](https://norabot.instatus.com/)", inline=None)

            await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        print(f'Ich wurde vom Server "{guild.name}" entfernt.')

def setup(bot):
    bot.add_cog(Welcome(bot))
