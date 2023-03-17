from abc import ABC, abstractmethod
from ..TwitchChatInterface.MessageHandler import Message
from ..TwitchChatInterface.TwitchChatInterface import TCI
class commandBase(ABC):
    def __init__(self, tci:TCI, message: Message, cmd:str) -> None:
        self.message = message
        self.tci = tci
        self.data = self.message.text.replace(cmd + " ", "")
        action = self.message.text.split(" ")[1] if len(self.message.text.split(" "))>1 else None
        if action in self.__dir__():
            self.data = self.data.replace(f"{action} ","")
            getattr(self, action)()
        else:
           self.print() 

    @abstractmethod
    def add(self):
        pass
    
    @abstractmethod
    def remove(self):
        pass
    
    @abstractmethod
    def print(self):
        pass