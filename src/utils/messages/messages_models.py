import discord
from discord.ext import commands

from src.config import config


async def generate_message_success(status: str, ctx: commands.Context) -> discord.Embed:
    embed: discord.Embed = discord.Embed(color = config["bot"]["messages"][f"{status}"]["color"])
    embed.set_footer(text = f"Команда {ctx.command.name} была выполнена успешно!")

    return embed


async def generate_message_error(ctx: commands.Context) -> discord.Embed:
    embed: discord.Embed = discord.Embed(color = config["bot"]["messages"]["error"]["color"])
    embed.set_footer(text = f"При выполнении команды {ctx.command.name} возникла ошибка!")

    return embed
