import discord
from discord.ext import commands

from src.config import config
from src.utils.messages import messages_models


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

        embed: discord.Embed = await messages_models.generate_message(status = "informational", ctx = ctx)
        embed.set_author(name = f"Приглашения {member.name}", icon_url = member.avatar_url)

        for invite in await ctx.guild.invites():
            if invite.inviter.id == member.id:
                embed.add_field(name = f"Приглашение {invite.code}", value = f"""Канал: {invite.channel.mention}
                                                                                Использований: {invite.uses}
                                                                                Создано: {invite.created_at.strftime(config["discord"]["interface"]["time_format"])}
                                                                                """, inline = False)

        await ctx.send(embed = embed)


def setup(bot: commands.Bot):
    bot.add_cog(Utilities(bot))
