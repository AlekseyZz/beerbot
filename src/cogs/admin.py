from discord.ext import commands

from src.utils.errors import errors_models


class Admin(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    # TODO: Сделай администраторские команды


def setup(bot: commands.Bot):
    bot.add_cog(Admin(bot))
