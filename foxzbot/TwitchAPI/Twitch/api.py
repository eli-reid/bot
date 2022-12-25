import requests
import asyncio
import aiohttp
import json
import webbrowser
from aiohttp import web



class TwitchAPI():
    def __init__(self) -> None:
        self._httpClientSession = aiohttp.ClientSession()
        self.__clientID = "l2fn9r2aceogfbjebk6ufcapa8s92q"
        self.__secret = "jc0b2fmf3qnldgko29ls2uu6q6ft0u"
        self._userCode = "0dwgf34olnh3toqays5jm6bgd4dbs2"
        self.__authorization
        self.__broadcasterID 
        self._get
        self._put = requests.api.put
        self._delete = requests.api.delete
        self._post = requests.api.post
        self._twitchURL = "https://api.twitch.tv/helix/"
        self._returnURL = "http://localhost:8000"
        
    async def getChatters(self)->json:
        endpoint = "/chat/chatters"
        params = {
            "broadcaster_id": "155181126",
            "moderator_id":"155181126",
            "first": "",
            "after": ""
        }
        headers ={
             'Authorization': 'Bearer 0dwgf34olnh3toqays5jm6bgd4dbs2',
             'Client-Id': 'l2fn9r2aceogfbjebk6ufcapa8s92q'
        }
        print(await self._httpClientSession.get("https://api.twitch.tv/helix/users?login=edog0049a"))
        await self._httpClientSession.get(self._twitchURL + endpoint,)

        return response.json()

async def Users(self):
        endpoint = ""
        params = {
            "broadcaster_id": "",
            "moderator_id":"",
            "first": "",
            "after": ""
        }
        headers ={
             'Authorization': 'Bearer kpvy3cjboyptmiacwr0c19hotn5s',
             'Client-Id': 'hof5gwx0su6owfn0nyan9c87zr6t'
        }
        
async def callback(request:web.Request):
    data = request.rel_url.query["code"]
    print(data)
    html ="""
    <html>
    <body>Hello</body></html>
    """
    return web.Response(content_type="html", body=html)

async def testapi ():
    wss = web.Application()
    wss.add_routes([web.get('/',callback), web.post('/',callback)])
    runner = web.AppRunner(wss)

    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8008)
    await site.start()

    url = "https://id.twitch.tv/oauth2/authorize?response_type=code&client_id=l2fn9r2aceogfbjebk6ufcapa8s92q&redirect_uri=http://localhost:8008/&scope=channel%3Amanage%3Apolls+channel%3Aread%3Apolls+moderator%3Aread%3Achatters"
    
    headers ={
            'Authorization': 'Bearer 9z1sj2g7e39rca90hztglu5uyt115l',
            'Client-Id': 'l2fn9r2aceogfbjebk6ufcapa8s92q',
            "broadcaster_id": "105580819",
            "moderator_id":"155181126",
            "first": "",
            "after": ""
        }
       
    t=aiohttp.ClientSession()
    wb = webbrowser.open_new(url=url)
    
    
    
    
    d = await t.get("https://api.twitch.tv/helix/chat/chatters?broadcaster_id=105580819&moderator_id=155181126",headers=headers)
    print(await d.json())
    while True:
       await asyncio.sleep(3600) 
