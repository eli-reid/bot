import json
from threading import Thread
from typing import Optional
import websockets
import asyncio
from websockets.server import serve, WebSocketServerProtocol
from django.urls import resolve
from enum import Enum
from .EventHandler import EventHandler
class WebSocketServer:

    def __init__(self) -> None:
        self.event: EventHandler = EventHandler
        self.__clients: dict[str,set[WebSocketServerProtocol]] = {}
        self.__url: str = 'localhost'
        self.__port: int = 8001
    
    async def broadcast(self, message: str, path: str): 
        if (self.__clients.get(path) is not None):
            for websocket in self.__clients.get(path).copy():
                try:
                    await websocket.send(message)
                except websockets.ConnectionClosed:
                    pass

    async def __messageHandler(self, websocket: WebSocketServerProtocol, path: str):
        if path not in self.__clients.keys():
            self.__clients[path] = set()
        self.__clients[path].add(websocket)
        async for message in websocket:
            dataDict:dict = json.loads(message)
            await self.event.emit(self, dataDict.get('EVENT'), dataDict.get('DATA'))
            
    async def __server(self):
        async with websockets.serve(self.__messageHandler, self.__url, self.__port):
            await asyncio.Future()

    def __runner(self):
        asyncio.run(self.__server())

    def run(self, url:Optional[str]=None, port:Optional[int]=None):
        self.__url: str = url if url is not None else self.__url
        self.__port: int = port if port is not None else self.__port
        newthread = Thread(target=self.__runner, daemon=True)
        newthread.start()
