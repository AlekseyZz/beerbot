from discord import Intents


config = {
        "bot": {
                "token": "token here",
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
                "cogs_path": "src.cogs"
        }
}