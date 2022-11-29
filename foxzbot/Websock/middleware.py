import asyncio

import websockets
from django.urls import resolve
from TCI.middleware import tci

async def wsMessageHandler(websocket):
    name = await websocket.recv()

    print(f"<<< {name}")
    tci.sendMessage("edog0049a", "hello")
    greeting = f"Hello {name}!"
    await websocket.send(greeting)
    print(websocket.id)
    print(websocket.path)
    print(f">>> {greeting}")

async def ws():
    await websockets.serve(wsMessageHandler, "localhost", 8001)
   