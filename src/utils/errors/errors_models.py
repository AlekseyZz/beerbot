from discord.ext import commands


class SubcommandIsNone(commands.CommandError):
    """
    Исключение, когда пользователь не указал подкоманду из группы команд
    """

    def __init__(self, commands_group):
        self.commands_group = commands_group


class CogImportError(commands.CommandError):
    """
    Исключение, когда ошибка при загрузке/отгрущзке/перезагрузке кога
    """

    def __init__(self, error_text):
        self.error_text = error_text
