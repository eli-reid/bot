from django.apps import apps
from random import choice
from ..MessageHandler import Message
from ..TwitchChatInterface import TCI
from .commandBase import commandBase
class command(commandBase):
    def __init__(self, tci: TCI, message: Message) -> None:
        self._commandObj = apps.get_model("Commands","Command")
        self._commandlist = list(self.commandObj.objects.all().values_list('command', flat=True))
        super().__init__(tci, message, "!command")

    def print(self):
        self.tci.sendMessage(self.message.channel,"command worked")

    def parseCommand(self):
        pass

    def add(self):
        pass

    def remove(self):
        pass
    
    @property.getter
    def commands(self)->list:
        return self._commandlist

    def isCommand(self, command:str)->bool:
        return command in self._commandlist 
        