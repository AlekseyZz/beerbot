import discord


config = {
        "bot": {
                "token": "take this on https://discord.com/developers",
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
                        "time_format": "%H:%M:%S %d.%m.%Y",
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
                }
        }
}
