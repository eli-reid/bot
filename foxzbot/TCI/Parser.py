from django.db import models
from django.apps import apps
from random import randint,choice
from .MessageHandler import Message
from .TwitchChatInterface import TCI
from .Builtins import commandBase
from .Builtins.quote import quote
from .Builtins.userCommands import userCommand
from .Builtins.command import command
from .Builtins.timerCommands import timer


def parser(message: Message, tci: TCI):
    if message.text.startswith("!"):
        commandText = message.text.split(" ")[0][1:]
        if commandText not in globals():
            command(tci,message)
        else:
            globals()[commandText](tci, message)