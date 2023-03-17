from django.apps import apps
from random import choice
from ..TwitchChatInterface.MessageHandler import Message
from ..TwitchChatInterface.TwitchChatInterface import TCI
from .commandBase import commandBase

class quote(commandBase):
    def __init__(self, tci:TCI, message: Message) -> None:
        self.quotesObj = apps.get_model("Quotes","Quotes")
        self.ids = list(self.quotesObj.objects.all().values_list('pk',flat=True))
        super().__init__(tci, message, "!quote")
       
        
    def print(self):
        try:
            if self.data is not None and self.data.isnumeric() and int(self.data) in self.ids:
                quoteobj = self.quotesObj.objects.get(id=self.data)
            else:
                quoteobj = self.quotesObj.objects.get(id=choice(self.ids))
             
            self.tci.sendMessage(self.message.channel,f"id: {quoteobj.id}, { quoteobj.quote}")
        except:
            pass

    def add(self):
        if self.data is not None:
            try:
                self.quotesObj.objects.get(quote=self.data).quote
                self.tci.sendMessage(self.message.channel,f"{self.data} has already been added!")
                return 
            except Exception:
                newQuote = self.quotesObj()
                newQuote.quote = self.data
                newQuote.save()
                self.tci.sendMessage(self.message.channel,"quote added")
    
    def remove(self):
        if self.data is not None and self.data.isnumeric() and int(self.data) in self.ids:
            self.quotesObj.objects.get(id=self.data).delete()
            self.tci.sendMessage(self.message.channel, f"Quote {self.data} Removed!")