from . import TwitchChatInterface
from .Parser import parser

settings={
  "server": "irc.chat.twitch.tv",
  "port": 6667,
  "user": "edog0049a",
  "password":"oauth:uqyosuh6zf54is2me2jl5l8qgahtlz",
  "channels": ["edog0049a"],
  "caprequest" :"twitch.tv/tags twitch.tv/commands twitch.tv/membership" 
}

tci = TwitchChatInterface.TCI(settings)

def handleDisconnect(sender,obj):
  print("disconnected")

def handleConnect(sender, obj):
    print ("connected!")

def handleMessage(sender, message):
    #print("[{0}] {1}: {2} ".format(message.channel,message.username,message.text))
    parser(message, sender)

def StartTciClient():
  tci.onConnected(handleConnect)
  tci.onMessage(handleMessage)
  tci.onDisconnected(handleDisconnect)
  tci.run()
