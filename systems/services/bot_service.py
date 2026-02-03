from systems.repositories.bot_repository import BotRepository
from systems.models import System


class BotService:
    @staticmethod
    def get_all(system: System):
        return BotRepository.get_all(system)
    
    @staticmethod
    def create_bot(data: dict, system: System):
        data["system"] = system
        return BotRepository.create_bot(data)
    
    @staticmethod
    def delete_bot():
        return BotRepository.delete_bot()