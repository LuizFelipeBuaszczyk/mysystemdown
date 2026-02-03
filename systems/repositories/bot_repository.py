from systems.models import Bot
from systems.models import System

class BotRepository:
    
    @staticmethod
    def get_all(system: System):
        return Bot.objects.filter(system=system)

    @staticmethod
    def create_bot(data: dict):
        return Bot.objects.create(**data)
    
    @staticmethod
    def delete_bot(bot: Bot):
        return bot.delete()