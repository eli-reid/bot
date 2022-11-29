from django.apps import apps
from random import randint,choice
from ..MessageHandler import Message
from ..TwitchChatInterface import TCI
class commandBase():
    def __init__(self, tci:TCI, message: Message) -> None:
        self.message = message
        self.tci = tci
    
    def add(self):
        raise NotImplementedError
    
    def remove(self):
        raise NotImplementedError
        