import discord
from discord.ext import commands
import os


from music_cog import music_cog

bot = commands.Bot(command_prefix='?')

@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready.")

bot.remove_command('help')

bot.add_cog(music_cog(bot))

bot.run("OTU4MTQ4NTYyOTEzNDkzMDcy.YkJHYg.wAfJ73dsvPvxWL282j5JksYtmL8")