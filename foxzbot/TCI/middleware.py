from time import sleep
from Websock.WebSocketServer import WebSocketServer
from . import TwitchChatInterface
from .Parser import parser
import asyncio
from django.apps import apps
import json
settings={
  "server": "irc.chat.twitch.tv",
  "port": 6667,
  "user": "edog0049a",
  "password":"oauth:uqyosuh6zf54is2me2jl5l8qgahtlz",
  "channels": ["edog0049a", "alilfoxz"],
  "caprequest" :"twitch.tv/tags twitch.tv/commands twitch.tv/membership" 
}

tci = TwitchChatInterface.TCI(settings)

def getChatStatusEventString() -> str:
  print(tci.channels)
  return json.dumps({'EVENT':'CHATSTATUS','DATA':tci.isConnected, 'ROOMS':list(tci.channels.keys()), 'BOTNAME':str(tci.globalUserState.display_name)})

async def handleChatStatus(sender, obj):
  await sender.broadcast(getChatStatusEventString(), "/chatstatus")
   
    
def StartTciClient():
  #setup websocket chat server command events
  Websock = apps.get_app_config("Websock")
  webSocketSever: WebSocketServer = Websock.websocketServer
  webSocketSever.event.on("CHATSTATUS", handleChatStatus)
  webSocketSever.event.on("CHATCONNECT", lambda sender, obj: tci.connect())
  webSocketSever.event.on("CHATDISCONNECT", lambda sender, obj: tci.disconnect())

  #setup chat server events
  tci.onConnected(lambda sender, obj: asyncio.run(Websock.broadcast(getChatStatusEventString(), "/chatstatus")))
  tci.onDisconnected(lambda sender, obj: asyncio.run(Websock.broadcast(getChatStatusEventString(), "/chatstatus")))
  tci.onGlobalUserState(lambda sender, obj: asyncio.run(Websock.broadcast(getChatStatusEventString(), "/chatstatus")))
  tci.onMessage(lambda sender, message: parser(message, sender))
  
  tci.run()
