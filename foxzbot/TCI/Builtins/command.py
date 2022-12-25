from django.apps import apps
from django.db.models import Model
from random import choice
from ..MessageHandler import Message
from ..TwitchChatInterface import TCI
from .commandBase import commandBase

class command(commandBase):

    def __init__(self, tci: TCI, message: Message) -> None:
        self._commandObj: Model = apps.get_model("Commands","Command")
        self._commandlist: list = list(self.commandObj.objects.all().values_list('command', flat=True))
        super().__init__(tci, message, "!command")

    def print(self) -> None:

        self.tci.sendMessage(self.message.channel,"command worked")

    def _parseCommand(self) -> None:
        """
        Parse List
        $userid - Username in lower case
        $username - display Username as normal
        $targetid - gtargets username in lower case
        $targetname - target username displayed as is
        $randuserid - gets random user from chat
        $botname - displays bot's name
        $arg1-$arg9 - gets position of whats after command
        $math[] - !math[1+7*6]
        $followage - gets months followed streamer
        """        
        
        if not self._checkCommand(""):
            self._parsedCommand["command"] =""
        else:
            self.tci.sendMessage(self.message.channel,f"{''} is a built-in command")

    def _checkCommand(self, command: str) -> bool:
        return command in globals().keys()

    def add(self) -> None:      
        pass

    def remove(self) -> None:
        pass

    def commands(self)->list:
        return self._commandlist

    def isCommand(self, command:str)->bool:
        return command in self._commandlist
 