import discord
import datetime
from discord.ext import commands

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.guild.id == 1231729975963553812:
            if member.bot:
                # Hier wird die Rolle für Bots zugewiesen
                role = member.guild.get_role(1026947232391512075)  # Rolle-ID für Bots einfügen
                await member.add_roles(role)

                embed = discord.Embed(title=f"{member.name} wurde hinzugefügt!",
                                      description=f"Die App {member.name} wurde hinzugefügt!\nNutze den Kanal <#1231730394123079740>",
                                      color=0xC84CE4)
                embed.set_thumbnail(url=str(member.display_avatar.url))
                embed.timestamp = datetime.datetime.now()
                embed.set_footer(text="Discord Welcome by Ciskyon | www.killerhase75.com")
                await self.bot.get_channel(1097205771667779596).send(embed=embed)
            else:
                embed = discord.Embed(title=f"{member.name} ist beigetreten!",
                                      description=f"❤️lich willkommen in unserer Community {member.name}! Wir wünschen dir viel Spaß auf dem Server! Wende dich bei Fragen oder Problemen gerne an unser Serverteam. Bitte schau auch unbedingt hier vorbei: <#988383474366967828>",
                                      color=0xC84CE4)
                embed.set_thumbnail(url=str(member.display_avatar.url))
                embed.timestamp = datetime.datetime.now()
                embed.set_footer(text="Discord Welcome by Ciskyon | www.killerhase75.com")
                await self.bot.get_channel(1097205771667779596).send(embed=embed)
        print("Wurde geladen!")

def setup(bot):
    bot.add_cog(Welcome(bot))
