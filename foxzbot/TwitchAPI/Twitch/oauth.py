import aiohttp
import asyncio
import json
import webbrowser
from datetime import datetime
from hashlib import md5
from aiohttp import web
from .utils import twitchErrors

class twitchOauth():
    OAUTH_URL = "https://id.twitch.tv/oauth2/"

    def __init__(self, client_id: str, client_secret: str, scope: str) -> None:
        self.onRequestData = lambda data: data
        self._client_id: str = client_id
        self._client_secret = client_secret
        self._scope = scope 
        self._redirectURL = f"http://localhost:8000/twitch/oauth/code"
        self.responseJson:json = None
        self._csrf = ""

    def getCodeURL(self, CSRF)->str:
        self._csrf = CSRF
        return f"{self.OAUTH_URL}authorize?response_type=code&client_id={self._client_id}&redirect_uri={self._redirectURL}&scope={self._scope}&state={CSRF}"

    async def getToken(self, code) -> str:
        url = f"{self.OAUTH_URL}token"
        data = {
                'client_id' : self._client_id,
                'client_secret' : self._client_secret,
                'code' : code,
                'grant_type' : 'authorization_code',
                'redirect_uri' : self._redirectURL                               
            }
        session = aiohttp.ClientSession()
        response: aiohttp.client.ClientResponse = await session.post(url=url,data=data)
        self.responseJson = await response.json()
        await session.close()
        return self.responseJson
