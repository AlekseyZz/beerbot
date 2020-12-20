from typing import Union

import discord
from discord.ext import commands

from src.config import config
from src.utils.messages import messages_models
from src.utils.errors import errors_models
from src.utils import time_formatter


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
                embed.add_field(name = f"Приглашение {invite.code}", value = (
                                                                    f"Канал: {invite.channel.mention}\n"
                                                                    f"Использований: {invite.uses}\n"
                                                                    f"Создано: {time_formatter.time_readable(invite.created_at)} ({time_formatter.timedelta_readable(invite.created_at)})\n"), inline = False)

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
                                usage = "information server [сервер: ID]")
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
        embed.add_field(name = "Общее:", value = (
                                                f"Создатель: {guild.owner.mention}\n"
                                                f"Сервер создан: {guild.created_at.strftime(config['discord']['interface']['time_format'])} ({time_formatter.timedelta_readable(guild.created_at)})\n"
                                                f"Регион: {config['discord']['regions'][guild.region]}\n"
                                                f"AFK канал: {guild.afk_channel or 'Отсутствует'}\n"
                                                f"Время AFK: {time_formatter.duration_readable(seconds = guild.afk_timeout)}\n"
                                                f"Канал системных сообщений: {guild.system_channel.mention}\n"
                                                f"Настройки уведомлений: {config['discord']['notifications_level'][guild.default_notifications]}\n"), inline = False)
        embed.add_field(name = "Статистика:", value = (
                                                f"Пользователей: {guild.member_count}\n"
                                                f"Текстовых каналов: {len(guild.text_channels)}\n"
                                                f"Голосовых каналов: {len(guild.voice_channels)}\n"
                                                f"Ролей: {len(guild.roles)}\n"
                                                f"Эмодзи: {len(guild.emojis)}\n"
f"Забанено: {len(await guild.bans())}"), inline = False)
        embed.add_field(name = "Модерация:", value = (
                                                f"Уровень проверки: {config['discord']['verification_level'][guild.verification_level]}\n"
                                                f"Фильтрация контента: {config['discord']['content_filter'][guild.explicit_content_filter]}\n"
                                                f"2FA для модерации: {config['discord']['interface']['enable_disable_icons'][guild.mfa_level]}\n"), inline = False)
        embed.add_field(name = "Состояние буста", value = (
                                                f"Уровень буста: {guild.premium_tier}\n"
                                                f"Количество бустов: {guild.premium_subscription_count}\n"
                                                f"Лимит эмодзи: {guild.emoji_limit}\n"
                                                f"Качество звука: {guild.bitrate_limit}\n"
                                                f"Анимированный аватар: {config['discord']['interface']['enable_disable_icons'][guild.is_icon_animated()]}\n"
                                                f"Лимит загрузки файлов: {guild.filesize_limit / 1024 ** 2} мегабайт"), inline = False)
        await ctx.send(embed = embed)

    @object_information.command(name = "role",
                                aliases = ("роль", "флаг", "flag"),
                                brief = "Команда для просмотра информации о роли",
                                usage = "information role [роль: ID, @упоминание, имя]")
    async def role(self, ctx: commands.Context, *, role: discord.Role = None) -> None:
        """
        Команда для просмотра информации о роли

        :param ctx: Контекст в котором вызывается команда (подробнее читать https://discordpy.readthedocs.io/en/neo-docs/ext/commands/api.html?highlight=context#discord.ext.commands.Context)
        :param role: Роль, для которой выводится информация
        :return: None
        """

        if role is None:
            role = ctx.author.top_role

        embed: discord.Embed = await messages_models.generate_message_success(status = "informational", ctx = ctx)
        embed.set_author(name = f"Роль {role.name}", icon_url = ctx.guild.icon_url)
        embed.add_field(name = "Общая информация:", value = (
                                                    f"ID роли: {role.id}\n"
                                                    f"Цвет: {role.color}\n"
                                                    f"Позиция: {role.position}\n"
                                                    f"Создана: {time_formatter.time_readable(role.created_at)} ({time_formatter.timedelta_readable(role.created_at)})\n"
                                                    f"Людей с ролью: {len(role.members)}"), inline = False)
        embed.add_field(name = "Настройки роли:", value = (
                                                    f"Показывать участников отдельно: {config['discord']['interface']['enable_disable_icons'][role.hoist]}\n"
                                                    f"Разрешать всем @упоминать роль: {config['discord']['interface']['enable_disable_icons'][role.mentionable]}"), inline = False)
        embed.add_field(name = "Права роли:", value = "\n".join(
                config["discord"]["permissions"][f"{permission}"] for permission, permission_allowed in role.permissions
                if permission_allowed), inline = False)
        await ctx.send(embed = embed)

    @object_information.command(name = "channel",
                                aliases = ("канал", "guild_channel", "сервер_канал"),
                                brief = "Команда для просмотра информации о канале",
                                usage = "information channel [канал: ID, #упоминание, имя]")
    async def channel(self, ctx: commands.Context, channel: Union[discord.TextChannel, discord.VoiceChannel] = None) -> None:
        """
        Команда для просмотра информации о роли

        :param ctx: Контекст в котором вызывается команда (подробнее читать https://discordpy.readthedocs.io/en/neo-docs/ext/commands/api.html?highlight=context#discord.ext.commands.Context)
        :param channel: Канал, для которого выводится информация
        :return: None
        """

        if channel is None:
            channel = ctx.channel

        embed: discord.Embed = await messages_models.generate_message_success(status = "informational", ctx = ctx)
        embed.set_author(name = f'Канал {channel.name}', icon_url = ctx.guild.icon_url)
        embed.add_field(name = "Общее:", value = (
                                        f"ID: {channel.id}\n"
                                        f"Создан: {time_formatter.time_readable(channel.created_at)} ({time_formatter.timedelta_readable(channel.created_at)})\n"
                                        f"Категория: {channel.category.name}\n"
                                        f"Позиция: {channel.position}"), inline = False)

        if isinstance(channel, discord.TextChannel):
            embed.add_field(name = f'{config["discord"]["channel_type"][channel.type]} Особенности:', value = (
                                        f"Описание: {channel.topic}\n"
                                        f"Задержка: {time_formatter.duration_readable(channel.slowmode_delay)}\n"
                                        f"Закреплённых сообщений: {len(await channel.pins())}"), inline = False)
        elif isinstance(channel, discord.VoiceChannel):
            embed.add_field(name = f'{config["discord"]["channel_type"][channel.type]} Особенности:', value = (
                                        f"Битрейт: {channel.bitrate}/сек\n"
                                        f"Лимит пользователей: {channel.user_limit}\n"
                                        f"Пользователей в канале: {len(channel.voice_states)}"), inline = False)

        await ctx.send(embed = embed)

    @object_information.command(name = "user",
                                aliases = ("member", "пользователь", "участник"),
                                brief = "Команда для просмотра информации о пользователе",
                                usage = "information user [пользователь: ID, @упоминание, имя, ник#дискриминатор]")
    async def user(self, ctx: commands.Context, user: discord.Member = None) -> None:
        """
        Команда для просмотра информации о пользователе

        :param ctx: Контекст в котором вызывается команда (подробнее читать https://discordpy.readthedocs.io/en/neo-docs/ext/commands/api.html?highlight=context#discord.ext.commands.Context)
        :param user: Пользователь, для которого выводится информация
        :return: None
        """

        if user is None:
            user = ctx.author

        embed: discord.Embed = await messages_models.generate_message_success(status = "informational", ctx = ctx)
        embed.set_author(name = f"Пользователь {user.name}", icon_url = user.avatar_url)
        embed.add_field(name = "Общее:", value = (
                                            f"ID: {user.id}"
                                            f"Статус: {config['discord']['status'][user.status]}\n"
                                            f"Создал аккаунт: {time_formatter.time_readable(user.created_at)} ({time_formatter.timedelta_readable(user.created_at)})\n"
                                            f"Присоединился: {time_formatter.time_readable(user.joined_at)} ({time_formatter.timedelta_readable(user.joined_at)})\n"
                                            f"Цвет: {user.color}"), inline = False)

        await ctx.send(embed = embed)


def setup(bot: commands.Bot):
    bot.add_cog(Utilities(bot))
