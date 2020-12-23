import discord
from discord.ext import commands

from src.utils.errors import errors_models
from src.utils.messages import messages_models
from src.utils import time_formatter


async def command_error_detection(ctx: commands.Context, error: commands.CommandError):
    async def command_error_message(problem, solution):
        embed: discord.Embed = await messages_models.generate_message_error(ctx = ctx)
        embed.add_field(name = "Проблема:", value = f"{problem}", inline = False)
        embed.add_field(name = "Решение:", value = f"{solution}", inline = False)
        await ctx.send(embed = embed)

    if isinstance(error, commands.CommandNotFound):
        pass

    elif isinstance(error, commands.DisabledCommand):
        await command_error_message(
                "Команда отключена!",
                "Используйте другую, активированную\n в данный момент команду",
        )

    elif isinstance(error, commands.CommandOnCooldown):

        await command_error_message(
                "Команда с задержкой!",
                f"Используйте данную команду \nчерез {time_formatter.duration_readable(error.retry_after)}",
        )

    elif isinstance(error, commands.MissingRequiredArgument):
        await command_error_message(
                "Вы упустили аргументы при\nиспользовании команды!",
                f"Запишите команду по синтаксису:\n`{ctx.bot.command_prefix}{ctx.command.usage}`"
        )

    elif isinstance(error, commands.BadArgument):
        await command_error_message(
                "Вы указали не существующий обьект!",
                f"Укажите существующий обьект при использовании:\n`{ctx.bot.command_prefix}{ctx.command.usage}`"
        )

    elif isinstance(error, discord.NotFound):
        await command_error_message(
                "Указанный обьект не был найден!",
                f"Укажите существующий обьект при использовании:\n`{ctx.bot.command_prefix}{ctx.command.usage}`"
        )
    elif isinstance(error, commands.NoPrivateMessage):
        await command_error_message(
                "Данную команду нельзя использовать в ЛС!",
                "Используйте данную команду на сервере"
        )
    elif isinstance(error, errors_models.SubcommandIsNone):
        await command_error_message(
                "Вы не указали подкоманду!",
                f"Укажите подкоманду из группы {error.commands_group}"
        )

    elif isinstance(error, errors_models.CogImportError):
        await command_error_message(
                "Ошибка при импортировании кога!",
                f"""Исправьте проблему:
                ```py
                {error.error_text}
                ```
                """
        )
    else:
        print(error)