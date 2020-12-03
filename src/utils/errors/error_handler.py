import discord
from discord.ext import commands

from src.utils.errors import error_models


async def command_error_detection(ctx: commands.Context, error):
    async def own_command_error_message(problem, solution):
        embed = discord.Embed()
        embed.add_field(name = "Проблема:", value = f"{problem}")
        embed.add_field(name = "Решение:", value = f"{solution}")
        await ctx.send(embed = embed)

    if isinstance(error, commands.CommandNotFound):
        await own_command_error_message(
                "Команда не найдена!",
                f"Используйте существующую команду,\nкоторая есть в списке `{ctx.bot.command_prefix}help`",
        )

    elif isinstance(error, commands.DisabledCommand):
        await own_command_error_message(
                "Команда отключена!",
                "Используйте другую, активированную\n в данный момент команду",
        )

    elif isinstance(error, commands.CommandOnCooldown):
        def make_readable(seconds):
            hours, seconds = divmod(seconds, 60 ** 2)
            minutes, seconds = divmod(seconds, 60)
            return f"{round(hours)} ч, {round(minutes)} мин, {round(seconds)} сек"

        await own_command_error_message(
                "Команда с задержкой!",
                f"Используйте данную команду \nпосле `{make_readable(error.retry_after)}` ⏳",
        )

    elif isinstance(error, commands.MissingRequiredArgument):
        await own_command_error_message(
                "Вы упустили аргументы при\nиспользовании команды!",
                f"Запишите команду по синтаксису:\n`{ctx.bot.command_prefix}{ctx.command.usage}`"
        )

    elif isinstance(error, commands.BadArgument):
        await own_command_error_message(
                "Вы указали не существующий обьект!",
                f"Укажите существующий обьект при использовании:\n`{ctx.bot.command_prefix}{ctx.command.usage}`"
        )

    elif isinstance(error, discord.NotFound):
        await own_command_error_message(
                "Указанный обьект не был найден!",
                f"Укажите существующий обьект при использовании:\n`{ctx.bot.command_prefix}{ctx.command.usage}`"
        )

    elif isinstance(error, error_models.SubcommandIsNone):
        await own_command_error_message(
                "Вы не указали подкоманду!",
                f"Укажите подкоманду из группы {error.commands_group}"
        )

    elif isinstance(error, error_models.CogImportError):
        await own_command_error_message(
                "Ошибка при импортировании кога!",
                f"""Исправьте проблему:
                ```py
                {error.error_text}
                ```
                """
        )