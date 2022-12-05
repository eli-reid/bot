from django.apps import apps
from random import randint,choice
from ..MessageHandler import Message
from ..TwitchChatInterface import TCI
class commandBase():
    def __init__(self, tci:TCI, message: Message, cmd:str) -> None:
        self.message = message
        self.tci = tci
        self.data = self.message.text.replace(cmd + " ", "")
        action = self.message.text.split(" ")[1] if len(self.message.text.split(" "))>1 else None
        if action in self.__dir__():
            self.data = self.data.replace(f"{action} ","")
            getattr(self,action)()
        else:
           self.print() 
    
    def add(self):
        raise NotImplementedError
    
    def remove(self):
        raise NotImplementedError

    def print(self):
        raise NotImplementedError