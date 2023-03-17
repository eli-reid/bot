from threading import Thread
from django.apps import apps
import json
from Websock.WebSocketServer import WebSocketServer
from asgiref.sync import sync_to_async

def updateSettings(message: str ):
    data:dict = json.loads(message)
    settings = apps.get_app_config('Home').get_model('Settings')

    setting = settings.objects.get(app='Stream Timer', key='time')
    setting.value = f"{data.get('Hr')}:{data.get('Min')}"
    setting.save()

    setting = settings.objects.get(app='Stream Timer', key='DisplayMsg')
    setting.value = f"{data.get('DisplayMsg')}"
    setting.save()

    
    setting = settings.objects.get(app='Stream Timer', key='EndMsg')
    setting.value = f"{data.get('EndMsg')}"
    setting.save()


async def handleTimerStart(sender, message: str):
    await sync_to_async(updateSettings)(json.loads(message).get("data"))
    await sender.broadcast(message,"/streamtimer")
    
async def handleTimerStop(sender, message: str ):
    await sender.broadcast(message, "/streamtimer")

async def handleTimerAddTime(sender,message):
    await sender.broadcast(message, "/streamtimer")


webSocketSever: WebSocketServer = apps.get_app_config("Websock").websocketServer
webSocketSever.event.on("STREAMTIMER_START", handleTimerStart)
webSocketSever.event.on("STREAMTIMER_STOP", handleTimerStop)
webSocketSever.event.on("STREAMTIMER_ADD", handleTimerAddTime)