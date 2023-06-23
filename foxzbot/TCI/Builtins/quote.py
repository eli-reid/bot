from django.apps import apps
from random import choice
from ..TwitchChatInterface.MessageHandler import Message
from ..TwitchChatInterface.TwitchChatInterface import TCI
from .commandBase import commandBase

class quote(commandBase):
    def __init__(self, tci:TCI, message: Message) -> None:
        self._quotesObj = apps.get_model("Quotes","Quotes")
        self._ids = list(self._quotesObj.objects.all().values_list('pk',flat=True))
        super().__init__(tci, message, "!quote")
       
    def print(self):
        try:
            if self.data is not None and self.data.isnumeric() and int(self.data) in self._ids:
                quoteobj = self._quotesObj.objects.get(id=self.data)
            else:
                quoteobj = self._quotesObj.objects.get(id=choice(self._ids))
            self.tci.sendMessage(self.message.channel,f"id: {quoteobj.id}, { quoteobj.quote}")
        except:
            pass

    def add(self):
        if self.data is not None and self._quotesObj.objects.filter(quote=self.data).count() > 0:
            self.tci.sendMessage(self.message.channel,f"{self.data} has already been added!")
        else:
            newQuote = self._quotesObj()
            newQuote.quote = self.data
            newQuote.save()
            self.tci.sendMessage(self.message.channel,"quote added")
    
    def remove(self):
        if self.data is not None and self.data.isnumeric() and int(self.data) in self._ids:
            self._quotesObj.objects.get(id=self.data).delete()
            self.tci.sendMessage(self.message.channel, f"Quote {self.data} Removed!")