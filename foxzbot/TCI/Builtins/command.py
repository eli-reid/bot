from django.apps import apps
from django.db.models import Model
from random import choice
from ..TwitchChatInterface.MessageHandler import Message
from ..TwitchChatInterface.TwitchChatInterface import TCI
from .commandBase import commandBase
from datetime import datetime, timedelta

class command(commandBase):

    def __init__(self, tci: TCI, message: Message) -> None:
        self._commandObj: Model = apps.get_model("Commands","Command")
        self._commandObjects = self._commandObj.objects.all()
        self._commandlist: list = list(self._commandObjects.values_list('command', flat=True))
        super().__init__(tci, message, "!command")

    def print(self) -> None:
       pass
            
    def add(self) -> None:      
        if self.data is not None and self._commandObjects.filter(command=self.data[0]).count() > 0:
            self.tci.sendMessage(self.message.channel,f"Command already exists")
        else:
            newCommand = self._commandObj()

            self.tci.sendMessage(self.message.channel,"quote added")

    def remove(self) -> None:
        pass

    def run(self, command):
        if self.isCommand(command) and not self.onCoolDown(command):
          commandObject: Model = self._commandObjects.filter(command=command)
          commandStr: str = self._parseCommand(commandData=commandObject.data)
          self.tci.sendMessage(self.message.channel,commandStr)
          
    def onCoolDown(self, command: str) -> bool:
        commandObject: Model = self._commandObjects.filter(command=command)
        return self.isCommand(command) and datetime.now() < commandObject.lastUsed + timedelta(commandObject.cooldown)

    @property
    def commands(self)->list:
        return self._commandlist

    def isCommand(self, command: str)->bool:
        return command in self._commandlist
    
    def _getCommandObject(self, command: str):
        return self._commandObjects.filter(command=command)
    
    def _parsNewCommand(self,commandData)-> dict:
        """
        cooldown
            +cd - cooldown followed by int
        rolerequired
            +rb - broadcaster
            +rm - mod
            +rs - subscriber
            +ra - any
        usage
            +uc - chatroom only 
            +uw - wisper only
            +ua - any
        """
        role: dict = {
            " +b ": "broadcaster",
            " +m ": "moderator",
            " +e ": "editor",
            " +s ": "subscriber",
            " +a ": "any"
       }
        
        usage: dict ={
            " SC ": "stream Chat",
            " SW ": "stream whisper",
            " SB ": "stream both"
        } 


        return dict()
    def _parseCommand(self, commandData) -> str:
        """
        Parse List
        $userid - Username in lower case
        $username - display Username as normal
        $targetid - targets username in lower case
        $targetname - target username displayed as is
        $randuserid - gets random user from chat
        $botname - displays bot's name
        $arg1-$arg9 - gets position of whats after command
        $math[] - !math[1+7*6]
        $followage - gets months followed streamer 'https://api.twitch.tv/helix/users/follows?to_id=23161357' this gets follwers of a person 
        TODO:
        target
        """ 
        data = commandData
        parseItems: dict = {
            "/me": "Bot",
            "$userid": self.message.username.lower(),
            "$username": self.message.username,
            "$botname": self.tci.globalUserState.display_name,
            "targetid": self.data[0]
        }

        for index, val in enumerate(self.data.split(" ")):
            if index + 1 > 9:
                break
            parseItems[f"$arg{index+1}"] = val
        
        for key, value in parseItems:
            data.replace(key,value)

        return data