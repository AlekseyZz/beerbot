import discord
from discord.ext import commands

from src.config import config
from src.utils.messages import messages_models
from src.utils.errors import errors_models


def make_readable(seconds):
    hours, seconds = divmod(seconds, 60 ** 2)
    minutes, seconds = divmod(seconds, 60)
    return f"{round(hours)} ч, {round(minutes)} мин, {round(seconds)} сек"


class Utilities(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name = "invites",
                      aliases = ("check_invites", "invites_check", "приглашения"),
                      brief = "Посмотреть приглашения пользователя и их статистику",
                      usage = "invites <участник: ID, @упоминание, никнейм, никнейм#дискриминатор>")
    async def user_invites(self, ctx: commands.Context, member: discord.Member = None) -> None:
        """
        Команда для просмотра приглашений пользователя: какие приглашения, их срок действия, сколько приглашено людей и прочие сведения.

        :param ctx: Контекст в котором вызывается команда (подробнее читать https://discordpy.readthedocs.io/en/neo-docs/ext/commands/api.html?highlight=context#discord.ext.commands.Context)
        :param member: Участник, приглашения которого надо посмотреть
        :return: None
        """

        if member is None:
            member = ctx.author

        embed: discord.Embed = await messages_models.generate_message_success(status = "informational", ctx = ctx)
        embed.set_author(name = f"Приглашения {member.name}", icon_url = member.avatar_url)

        for invite in await ctx.guild.invites():
            if invite.inviter.id == member.id:
                embed.add_field(name = f"Приглашение {invite.code}", value = f"""Канал: {invite.channel.mention}
                                                                    Использований: {invite.uses}
                                                                    Создано: {invite.created_at.strftime(config["discord"]["interface"]["time_format"])}
                                                                    """, inline = False)

        await ctx.send(embed = embed)

    @commands.group(name = "information",
                    aliases = ("информация", "инфо", "info"),
                    brief = "Группа команд для просмотра информации об обьекте",
                    usage = "information <тип обьекта> <обьект>")
    async def object_information(self, ctx: commands.Context) -> None:
        """
        Группа команд для просмотра информации об обьекте (канале, роли, эмодзи)

        :param ctx: Контекст в котором вызывается команда (подробнее читать https://discordpy.readthedocs.io/en/neo-docs/ext/commands/api.html?highlight=context#discord.ext.commands.Context)
        :return: None
        """

        if ctx.invoked_subcommand is None:
            raise errors_models.SubcommandIsNone(ctx.command)

    @object_information.command(name = "server",
                                aliases = ("сервер", "гильдия", "guild"),
                                brief = "Команда для просмотра информации о сервере",
                                usage = "information server [сервер: ID, имя]")
    async def server(self, ctx: commands.Context, *, guild: discord.Guild = None) -> None:
        """
        Команда для просмотра информации о сервере

        :param ctx: Контекст в котором вызывается команда (подробнее читать https://discordpy.readthedocs.io/en/neo-docs/ext/commands/api.html?highlight=context#discord.ext.commands.Context)
        :param guild: Сервер, для которого выводится информация
        :return: None
        """

        if guild is None:
            guild = ctx.guild

        embed: discord.Embed = await messages_models.generate_message_success(status = "informational", ctx = ctx)
        embed.set_author(name = f"Сервер {guild.name}", icon_url = guild.icon_url)
        embed.add_field(name = "Общее:", value = f"""Создатель: {guild.owner.mention}
                                                    Регион: {config["discord"]["regions"][guild.region]}
                                                    AFK канал: {guild.afk_channel}
                                                    Время AFK: {make_readable(guild.afk_timeout)}
                                                    Канал системных сообщений: {guild.system_channel.mention}
                                                    Настройки уведомлений: {config["discord"]["notifications_level"][guild.default_notifications]}
                                                    """, inline = False)
        embed.add_field(name = "Статистика:", value = f"""Пользователей: {guild.member_count}
                                                    Текстовых каналов: {len(guild.text_channels)}
                                                    Голосовых каналов: {len(guild.voice_channels)}
                                                    Ролей: {len(guild.roles)}
                                                    Эмодзи: {len(guild.emojis)}
                                                    Забанено: {len(await guild.bans())}""")
        embed.add_field(name = "Модерация:",
                        value = f"""Уровень проверки: {config["discord"]["verification_level"][guild.verification_level]}
                                                    Фильтрация контента: {config["discord"]["content_filter"][guild.explicit_content_filter]}
                                                    2FA для модерации: {config["discord"]["interface"]["enable_disable_icons"][guild.mfa_level]}
                                                    """, inline = False)
        embed.add_field(name = "Состояние буста", value = f"""Уровень буста: {guild.premium_tier}
                                                    Количество бустов: {guild.premium_subscription_count}
                                                    Лимит эмодзи: {guild.emoji_limit}
                                                    Качество звука: {guild.bitrate_limit}
                                                    Анимированный аватар: {config["discord"]["interface"]["enable_disable_icons"][guild.is_icon_animated()]}
                                                    Лимит загрузки файлов: {guild.filesize_limit / 1024 ** 2} мегабайт""",
                        inline = False)
        await ctx.send(embed = embed)


def setup(bot: commands.Bot):
    bot.add_cog(Utilities(bot))
