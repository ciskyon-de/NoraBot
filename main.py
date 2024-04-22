import datetime
import discord
import os
from dotenv import load_dotenv
from discord.ext import tasks, commands
import asyncio
import ciscord






# Discord Berechtigung
intents = discord.Intents.all()
bot = commands.Bot(intents=intents, command_prefix=":")

# Bot Start-Event

@bot.event
async def on_ready() -> None:
    status_task.start()
    print(f"{ciscord.abstand}")
    print(f"{ciscord.Modname}")
    print(f"{ciscord.Version}")
    print(f"{ciscord.Inhaber}")
    print(f"{ciscord.Lastupdate}")
    print(f"{ciscord.abstand}")
    print(f"{ciscord.Botname}")
    print(f"{ciscord.Botversion}")
    print(f"{ciscord.Devs}")
    print(f"{ciscord.Support}")
    print(f"{ciscord.online}")
    print(f"{ciscord.abstand}")
    print(f"{ciscord.Service_serverlink}")
    print(f"{ciscord.Service_Botlink}")
    print(f"{ciscord.abstand}")


@tasks.loop()

async def status_task() -> None:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"Spotify"))
        await asyncio.sleep(20)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"Babalos - Snow Crystal [HQ]"))
        await asyncio.sleep(20)




if __name__ == "__main__":
    load_dotenv()



    bot.load_extension(f"{ciscord.Load_botinfo}")
    bot.load_extension(f"{ciscord.Load_einladen}")
    bot.load_extension(f"cogs.willkommen")




    bot.run(os.getenv(f"NoraBot"))


