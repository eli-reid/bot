import asyncio
from websockets import client
from .EventHandler import EventHandler
class WSClient:
    def __init__(self) -> None:
        self.connection = None
        self.event: EventHandler = EventHandler
       
    async def _connect(self, path):
       async with client.connect() as self.connection:
        self._messageHandler(await self.connection.recv())   
        self.connection.keepalive_ping() 

    async def send(self, msg, path = "all"):
        await self.connection.send(msg)

    async def _messageHandler(self, message):
        pass
    