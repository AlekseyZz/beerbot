from discord import Intents


config = {
        "bot": {
                "token": "generate token of bot on https:discord.com/developers",
                "settings": {
                        "command_prefix": "$",
                        "case_insensitive": True,
                        "intents": Intents.all()
                },
                "messages": {
                        "success": {
                                "color": 108734,
                                "text": "Успешно"
                        },
                        "error": {
                                "color": 871034,
                                "text": "Безуспешно"
                        }
                },
                "cogs": ["admin", "utilities"],
                "cogs_path": "cogs"
        },
        "discord": {
                "regions": {
                        "amsterdam": ":flag_nl: Амстердам",
                        "brazil": ":flag_br: Бразилия",
                        "dubai": ":flag_ae: Дубаи",
                        "eu_central": ":flag_eu: Центральный Евросоюз",
                        "eu_west": ":flag_eu: Западный Евросоюз",
                        "europe": ":flag_eu: Европа",
                        "frankfurt": ":flag_de: Франкфурт",
                        "hongkong": ":flag_hk: Гонконг",
                        "india": ":flag_in: Индия",
                        "japan": ":flag_jp: Япония",
                        "london": ":flag_gb: Лондон",
                        "russia": ":flag_ru: Россия",
                        "singapore": ":flag_sg: Сингапур",
                        "southafrica": ":flag_za: Южная Африка",
                        "south_korea": ":flag_hk: Южная Корея",
                        "sydney": ":flag_au: Сидней",
                        "us_central": ":flag_us: Центральный США",
                        "us_east": ":flag_us: Восточный США",
                        "us_south": ":flag_us: Южный США",
                        "us_west": ":flag_us: Западный США",
                        "vip_amsterdam": "VIP Амстердам",
                        "vip_us_east": ":flag_us: VIP Восточный США",
                        "vip_us_west": ":flag_us: VIP Западный США"
                },
                "interface": {
                        "time_format": "%H:%M:%S %d.%m.%Y"
                }
        }
}


