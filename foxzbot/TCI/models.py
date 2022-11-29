from django.db import models
from django.apps import apps
from random import randint,choice
from .MessageHandler import Message
from .TwitchChatInterface import TCI
from .Builtins import commandBase
from .Builtins.quote import quote

def parser(message: Message, tci: TCI):
    if message.text.startswith("!"):
        command = message.text.split(" ")[0][1:]
        if command not in globals():
            print ("not built command")
        else:
             globals()[command](tci, message)