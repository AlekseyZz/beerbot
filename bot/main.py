import discord
from discord.ext import commands
import json


with open("config.json", "r") as config_read:
    config = json.load(config_read)

bot = commands.Bot(config['bot']['prefix'], case_insensitive = True, intents = discord.Intents.all())


@bot.event
async def on_ready():
    print(f"{bot.user} запущен, ID: {bot.user.id}")

if __name__ == "__main__":
    bot.run(config['discord']['token'])