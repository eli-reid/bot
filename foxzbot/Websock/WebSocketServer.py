import json
from threading import Thread
from types import NoneType
import websockets
import asyncio
from websockets.server import serve
from django.urls import resolve
from TCI.middleware import tci
from enum import Enum

class WebSocketServer:
    class EVENT(Enum):
        BROADCAST = 1

    def __init__(self) -> None:
        self.__clients: dict[str,set] = {}
        self.__url: str = 'localhost'
        self.__port: int = 8001
    
    async def broadcast(self, message, path):
        if (self.__clients.get(path) is not None):
            for websocket in self.__clients.get(path).copy():
                try:
                    await websocket.send(message)
                except websockets.ConnectionClosed:
                    pass

    async def __messageHandler(self,websocket, path:str):
        if path not in self.__clients.keys():
            self.__clients[path] = set()
        self.__clients[path].add(websocket)
        async for msg in websocket:
            dataDict:dict = json.loads(msg)
            if dataDict['EVENT'] == self.EVENT.BROADCAST.value:
                await self.broadcast(dataDict['data'], path)
        
    async def __server(self):
        async with websockets.serve(self.__messageHandler, self.__url, self.__port):
            await asyncio.Future()

    def __runner(self):
        asyncio.run(self.__server())

    def run(self, url:str or NoneType=None, port:int or NoneType =None):
        self.__url: str = url if url is not None else self.__url
        self.__port: int = port if port is not None else self.__port
        newthread = Thread(target=self.__runner, daemon=True)
        newthread.start()
