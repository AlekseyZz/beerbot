import os
import site
site.addsitedir(os.path.dirname(os.getcwd()))

import discord
from discord.ext import commands

from src.utils.loaders import cogs_loader
from src.utils.errors import errors_models
from src.utils.errors import errors_handler
from src.utils.messages import messages_models
from src.config import config

bot = commands.Bot(**config["bot"]["settings"])


@bot.event
async def on_ready() -> None:
    print(f"{bot.user} запущен, ID: {bot.user.id}")
    cogs_loader.loading_cogs(bot = bot, cogs = config["bot"]["cogs"])


@bot.event
async def on_command_error(ctx: commands.Context, error: commands.CommandError) -> None:
    await errors_handler.command_error_detection(ctx, error)


@bot.group(name = "cog",
           aliases = ("modules", "module", "модули", "модуль"))
@commands.is_owner()
async def cogs(ctx: commands.Context) -> None:
    """
    Создание группы команд для работы с когами (подмодулями) бота.

    :param ctx: Контекст в котором вызывается команда (подробнее читать https://discordpy.readthedocs.io/en/neo-docs/ext/commands/api.html?highlight=context#discord.ext.commands.Context)
    :return: None
    """

    if ctx.invoked_subcommand is None:
        raise errors_models.SubcommandIsNone(ctx.command)


@cogs.command(name = "load",
              aliases = ("loading", "загрузить", "догрузить", "загрузка", "догрузка"),
              brief = "Загрузить ког",
              usage = "cog load <название кога: строка>")
async def cogs_load(ctx: commands.Context, cog: str) -> None:
    """
    Команда для загрузки кога (подмодуля) в боте.

    :param ctx: Контекст в котором вызывается команда (подробнее читать https://discordpy.readthedocs.io/en/neo-docs/ext/commands/api.html?highlight=context#discord.ext.commands.Context)
    :param cog: Подмодуль бота, который требуется загрузить
    :return: None
    """

    try:
        bot.load_extension(f'{config["bot"]["cogs_path"]}.{cog}')

        embed: discord.Embed = await messages_models.generate_message_success(status = "success", ctx = ctx)
        embed.set_author(name = f"Загрузка кога {cog}", icon_url = bot.user.avatar_url)
        await ctx.send(embed = embed)
    except (ImportError, AttributeError) as error:
        raise errors_models.CogImportError(error)


@cogs.command(name = "unload",
              aliases = ("unloading", "отгрузить", "отгрузка"),
              brief = "Отгрузить ког",
              usage = "cog unload <название кога: строка>")
async def cogs_unload(ctx: commands, cog: str) -> None:
    """
    Команда для отгрузки кога (подмодуля) в боте.

    :param ctx: Контекст в котором вызывается команда (подробнее читать https://discordpy.readthedocs.io/en/neo-docs/ext/commands/api.html?highlight=context#discord.ext.commands.Context)
    :param cog: Подмодуль бота, который требуется отгрузить
    :return: None
    """

    try:
        bot.unload_extension(f'{config["bot"]["cogs_path"]}.{cog}')

        embed: discord.Embed = await messages_models.generate_message_success(status = "success", ctx = ctx)
        embed.set_author(name = f"Отгрузка кога {cog}", icon_url = bot.user.avatar_url)
        await ctx.send(embed = embed)
    except (ImportError, AttributeError) as error:
        raise errors_models.CogImportError(error)


@cogs.command(name = "reload",
              aliases = ("reloading", "перезагрузить", "перезагрузка"),
              brief = "Перезагрузить ког",
              usage = "cog reload <название кога: строка>")
async def cogs_reload(ctx: commands.Context, cog: str) -> None:
    """
    Команда для перезагрузки кога (подмодуля) в боте.

    :param ctx: Контекст в котором вызывается команда (подробнее читать https://discordpy.readthedocs.io/en/neo-docs/ext/commands/api.html?highlight=context#discord.ext.commands.Context)
    :param cog: Подмодуль бота, который требуется перезагрузить
    :return: None
    """

    try:
        bot.reload_extension(f'{config["bot"]["cogs_path"]}.{cog}')

        embed: discord.Embed = await messages_models.generate_message_success(status = "success", ctx = ctx)
        embed.set_author(name = f"Перезагрузка кога {cog}", icon_url = bot.user.avatar_url)
        await ctx.send(embed = embed)
    except (ImportError, AttributeError) as error:
        raise errors_models.CogImportError(error)


if __name__ == "__main__":
    bot.run(config["bot"]["token"])
