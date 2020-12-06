import discord
from discord.ext import commands

from src.config import config


async def generate_message(status: str, ctx: commands.Context) -> discord.Embed:
    embed: discord.Embed = discord.Embed(color = config["bot"]["messages"][f"{status}"]["color"])
    embed.set_footer(text = f"Команда {ctx.command.name} была выполнена успешно!")

    return embed
