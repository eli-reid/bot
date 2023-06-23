from Websock.WebSocketServer import WebSocketServer
from .TwitchChatInterface.TwitchChatInterface import TCI
from .Parser import parser
import asyncio
from django.apps import apps
from django.conf import settings as app_settings

import json

#setup tci 
settings={
"server": "",
"port": 0,
"user": "",
"password":"",
"channels": [],
"caprequest" :""
}
tci =  TCI(settings)

def getChatStatusEventString() -> str:
  return json.dumps({'EVENT':'CHATSTATUS','DATA':tci.isConnected, 'ROOMS':list(tci.channels.keys()), 'BOTNAME':str(tci.globalUserState.display_name)})

def handleDisconnect(sender,obj):
  print("disconnected")

def handleConnect(sender, obj):
    print ("connected!")
async def handleChatStatus(sender, obj):
  await sender.broadcast(getChatStatusEventString(), "/chatstatus")

def loadTCISettings():
    #loads settings into tci from settings database once app is ready
    settingsOBJ = apps.get_app_config('Home').get_model('Settings')
    settings={
    
        "server": settingsOBJ.objects.get(app='Chat Interface', key='Server').value,
        "port": int(settingsOBJ.objects.get(app='Chat Interface', key='Port').value),
        "user": settingsOBJ.objects.get(app='Chat Interface', key='User').value,
        "password":f"oauth:{settingsOBJ.objects.get(app='Chat Interface', key='OAuth Key').value}",
        "channels": str(settingsOBJ.objects.get(app='Chat Interface', key='channels').value).split(','),
        "caprequest" : settingsOBJ.objects.get(app='Chat Interface', key='caprequest').value
    }
    tci.updateSettings(settings)

    
def StartTciClient():
  tci.onConnected(handleConnect)
  tci.onMessage(handleMessage)
  tci.onDisconnected(handleDisconnect)
  
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
  tci.onMessage(parser)
  
  tci.run()
