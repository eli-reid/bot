import asyncio
import json
import websockets
from websockets import connection
from django.urls import resolve
from TCI.middleware import tci
def EventData():
    Settings = {
    "P_setmsg": "Moderator",
    "P_settime": "Moderator",
    "P_addhr": "Moderator",
    "P_stop": "Moderator",
    "ChatEndEnabled": True,
    "ChatSoonEnabled": True,
    "DisplayMsg": "Stream Ends In: ",
    "P_timeleft": "Moderator",
    "P_gettime": "Moderator",
    "EndMsg": "Stream Ends In: ",
    "EndTime": "00:30:00",
    "P_start": "Moderator",
    "AutoStart": True,
    "ChatSoonMsg": "@everyone, i'm going to select the winner In $min minutes!",
    "ChatSoonSlider": 15.0,
    "P_addmin": "Moderator",
    "P_setendmsg": "Moderator",
    "ChatEndMsg": "@everyone, lets pick a winner",
    "SoundEnabled": True,
    "SoundFile": "It's Time For Bed.mp3",
    "SoundVolume": 50.0,
    "Color1": "rgba(255,0,0,255)",
    "Color2": "rgba(230,126,34,1)",
    "Color3": "rgba(255,0,0,255)",
    "Color4": "rgba(230,126,34,1)",
    "Color5": "rgba(230,126,34,1)",
    "Color6": "rgba(179,34,230,1)",
    "Color7": "rgba(85,34,230,1)",
    "APIKey": "",
    "InTransition": "SlideRight",
    "OutTransition": "SlideRight",
    "Duration": 5
    }
    eventDATA={}
    t=Settings["EndTime"].split(":")
    eventDATA["Hr"] = t[0]
    eventDATA["Min"] = t[1]
    eventDATA["DisplayMsg"] = Settings["DisplayMsg"]
    eventDATA["EndMsg"] = Settings["EndMsg"]
    return json.dumps(eventDATA)

async def wsMessageHandler(websocket):
    name = await websocket.recv()
    
    print(f"<<< {name}")
    greeting = f"Hello {name}!"
    test = {"event":"EVENT_START","data":EventData()}
    #await websocket.send(greeting)
    await websocket.send(json.dumps(test))
    print(websocket.id)
    print(websocket.path)
    print(f">>> {greeting}")

async def ws():
    await websockets.serve(wsMessageHandler, "localhost", 8001)
   c

