from django.db import models
from django.apps import apps
from random import randint,choice
from .TwitchChatInterface.MessageHandler import Message
from .TwitchChatInterface.TwitchChatInterface import TCI
from .Builtins import commandBase
from .Builtins.quote import quote
from .Builtins.userCommands import userCommand
from .Builtins.command import command
from .Builtins.timerCommands import timer


def parser(tci: TCI, message: Message):
    print(message.raw)
    if message.text.startswith("!"):
        commandText = message.text.split(" ")[0][1:]
        if commandText in globals():
            globals()[commandText](tci, message)
    else:
        command(tci, message).run(message.text.split(" ")[0])
       