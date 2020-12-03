from discord.ext import commands

from src.config import config


def loading_cogs(bot: commands.Bot, cogs: list) -> None:
    """
    Функция для загрузки когов (подмодулей) бота.

    :param bot: Бот, в котором следует загрузить коги.
    :param cogs: Список когов для загрузки
    :return: None
    """

    for cog in cogs:
        try:
            bot.load_extension(f'{config["bot"]["cogs_path"]}.{cog}')
            print(f"Ког {cog} был успешно загружен!")
        except (ImportError, AttributeError) as error:
            print(f"При загрузке кога {cog} произошла ошибка:\n{error}")
