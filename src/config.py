import os
import discord


config = {
        "bot": {
                "token": os.environ.get("TOKEN"),
                "settings": {
                        "command_prefix": "$",
                        "case_insensitive": True,
                        "intents": discord.Intents.all()
                },
                "messages": {
                        "success": {
                                "color": 0x00CC6A,
                        },
                        "error": {
                                "color": 0xE74856,
                        },
                        "informational": {
                                "color": 0x0099BC
                        }
                },
                "cogs": ["admin", "utilities"],
                "cogs_path": "cogs"
        },
        "discord": {
                "permissions": {
                        "create_instant_invite": "Создавать приглашения",
                        "add_reactions": "Добавлять реакции",
                        "administrator": "Администратор",
                        "attach_files": "Прикреплять файлы",
                        "ban_members": "Блокировать участников",
                        "change_nickname": "Изменять никнейм",
                        "connect": "Подключаться",
                        "deafen_members": "Отключать звук участникам",
                        "embed_links": "Вставлять ссылки",
                        "external_emojis": "Использовать эмодзи с других серверов",
                        "kick_members": "Выгонять участников",
                        "manage_channels": "Управлять каналами",
                        "manage_emojis": "Управлять эмодзи",
                        "manage_guild": "Управлять сервером",
                        "manage_messages": "Управлять сообщениями",
                        "manage_nicknames": "Управлять никнеймами",
                        "manage_permissions": "Управлять ролями",
                        "manage_roles": "Управлять ролями",
                        "manage_webhooks": "Управлять вебхуками",
                        "mention_everyone": "Упоминать @everyone, @here и все роли",
                        "move_members": "Перемещать участников",
                        "mute_members": "Отключать голос участникам",
                        "priority_speaker": "Приоритетный голос",
                        "read_message_history": "Читать историю сообщений",
                        "read_messages": "Читать сообщения",
                        "send_messages": "Отправлять сообщения",
                        "send_tts_messages": "Отправлять tts-сообщения",
                        "speak": "Говорить",
                        "stream": "Видео",
                        "use_external_emojis": "Использовать эмодзи с других серверов",
                        "use_voice_activation": "Активация по голосу",
                        "view_audit_log": "Просмотр журнала аудита",
                        "view_channel": "Просматривать канал",
                        "view_guild_insights": "Смотреть аналитику сервера"
                },
                "regions": {
                        discord.VoiceRegion("amsterdam"): "Амстердам :flag_nl:",
                        discord.VoiceRegion("brazil"): "Бразилия :flag_br:",
                        discord.VoiceRegion("dubai"): "Дубаи :flag_ae:",
                        discord.VoiceRegion("europe"): "Европа :flag_eu:",
                        discord.VoiceRegion("frankfurt"): "Франкфурт :flag_de:",
                        discord.VoiceRegion("hongkong"): "Гонконг :flag_hk:",
                        discord.VoiceRegion("india"): "Индия :flag_in:",
                        discord.VoiceRegion("japan"): "Япония :flag_jp:",
                        discord.VoiceRegion("london"): "Лондон :flag_gb:",
                        discord.VoiceRegion("russia"): "Россия :flag_ru:",
                        discord.VoiceRegion("singapore"): "Сингапур :flag_sg:",
                        discord.VoiceRegion("southafrica"): "Южная Африка :flag_za:",
                        discord.VoiceRegion("sydney"): "Сидней :flag_au:",
                },
                "interface": {
                        "time_local": "ru",
                        "time_format": "%d.%m.%Y %H:%M:%S",
                        "enable_disable_icons": {
                                True: "<:discord_on:763327382659661835>",
                                False: "<:discord_off:763327382672113664>"
                        }
                },
                "content_filter": {
                        discord.ContentFilter(0): "<:discord_off:763327382672113664>",
                        discord.ContentFilter(1): "Для участников без ролей",
                        discord.ContentFilter(2): "Для всех участников"
                },
                "verification_level": {
                        discord.VerificationLevel(0): "(Пусто) Нету",
                        discord.VerificationLevel(1): "(Низкий) Подтверждённый по e-mail аккаунт",
                        discord.VerificationLevel(2): "(Средний) Также быть 5 минут зарегистрированным в Discord",
                        discord.VerificationLevel(3): "(Высокий) Также быть на сервере минимум 10 минут",
                        discord.VerificationLevel(4): "(Экстремальный) Подтверждённый по номеру телефона аккаунт"
                },
                "notifications_level": {
                        discord.NotificationLevel(0): "Все сообщения",
                        discord.NotificationLevel(1): "Только @упоминания"
                },
                "channel_type": {
                        discord.ChannelType(0): "<:text_channel:715235724525437062>",
                        discord.ChannelType(2): "<:voice_channel:764559925220343860>",
                        discord.ChannelType(5): "<:announcements_channel:764559906241511434>"
                },
                "status": {
                        discord.Status("online"): "<:online:789898968938709002> В сети",
                        discord.Status("offline"): "<:offline:789898968737382441> не в сети",
                        discord.Status("invisible"): "<:offline:789898968737382441> Невидимый",
                        discord.Status("dnd"): "<:dnd:789898968883920927> Не беспокоить",
                        discord.Status("idle"): "<:idle:789898968632524831> Не активен",
                },
                "user_flags": {
                        "hypesquad_bravery": "<:bravery:726110786233040906>",
                        "hypesquad_brilliance": "<:brilliance:726110786229108768>",
                        "hypesquad_balance": "<:balance:726110785654358036>",
                        "verified_bot_developer": "<:verified_bot_developer:791240612996710400>",
                        "early_verified_bot_developer": "<:verified_bot_developer:791240612996710400>"
                }
        }
}
