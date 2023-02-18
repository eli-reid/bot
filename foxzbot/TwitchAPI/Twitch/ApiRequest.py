from typing import Optional,Callable
import asyncio
import aiohttp
import json
from aiohttp import web

class APIRequest():
    def __init__(self, apiURL:str, returnURL:Optional[str]=None, returnPort: Optional[int]=None) -> None:
        self._httpClientSession = aiohttp.ClientSession()
        self._apiURL = apiURL
        self._returnURL = returnURL if returnURL else "http://localhost" 
        self._returnPort = returnPort if returnPort else 8880

    async def getRequest(self, endPoint:str, headers:Optional[dict[str,str]]=None, callbacks:dict[str,Callable]=None, **kwargs) -> json:
        """
        getRequest
            * endPoint -> str: location  of api call 
            * headers -> dict[str, str]: for any haeaders reqiured by api 
            * callbacks -> dict[Method, function] 
                * method: str  "GET", "POST", ...
                * funcion: async callback(request) - request accepts a aiohttp.web.Request
        """
        if len(callbacks.keys()):
            callbackServer = CallbackServer("/callback", callbacks, self._returnURL, self._returnPort)
            await callbackServer.start()
        response = await self._httpClientSession.get(url=self._apiURL + endPoint, headers=headers, kwargs=kwargs)
        return response.json()

    async def postRequest(self, endPoint:str, headers:Optional[dict]=None, callbacks:dict[str,Callable]=None, **kwargs) -> json:
        """
        postRequest
            * endPoint -> str: location  of api call 
            * headers -> dict[str, str]: for any haeaders reqiured by api 
            * callbacks -> dict[Method, function] 
                * method: str  "GET", "POST", ...
                * funcion: async callback(request) - request accepts a aiohttp.web.Request
        """
        if len(callbacks.keys()):
            callbackServer = CallbackServer("/callback", callbacks, self._returnURL, self._returnPort)
            await callbackServer.start()
        response = await self._httpClientSession.post(url=self._apiURL + endPoint, headers=headers, kwargs=kwargs)
        return response.json()


class CallbackServer():
    def __init__(self, path:str, callbacks:dict[str, Callable], host:Optional[str]=None, port:Optional[int]=None) -> None:
        """
        callbacks dict[method as string, callback function]
        """
        self._webserver:web.Application = web.Application()
        self._routes: list = []
        self._host: str = host if host else "localhost"
        self._port: int = port if port else 8880
        self._run: bool = True
        self._runner = web.AppRunner(self._webserver)
        self._server: web.TCPSite
        for method, handler in callbacks:
            self._webserver.router.add_route(method=method.upper(), path=path, handler=handler)

    async def start(self) -> None:
        await self._runner.setup()
        self._server = web.TCPSite(runner=self._runner, host=self._host, port=self._port)
        await self._server.start()
        while self._run:
            await asyncio.sleep(120) 
   
    async def stop(self):
        await self._server.stop()
        self._run = False
        