from Resources.Utils import pagenation, dateRange, RequestBaseClass, ResponseBaseClase
from Resources import Analytics, Ads
from ApiRequest import APIRequest
import json
from typing import Tuple
class APIReqestFailedException(Exception):
     pass

class twitchAPI:
    def __init__(self, client_id:str, client_credentials:str, access_token:str) -> None:
        self._APIRequest: APIRequest = APIRequest("https://api.twitch.tv/helix/")
        self._client_id: str = client_id
        self._client_credentials: str = access_token
        self._access_token: str = access_token


    async def StartCommercial(self) -> Ads.StartCommercialRepsonse:
        request = Ads.StartCommercialRequest()
        response = Ads.StartCommercialRepsonse()
        await self.twitchAPICall(request, response)
        return response

    async def GetExtensionAnalytics(self) -> Analytics.ExtensionAnalyticsResponse:
        request = Analytics.ExtensionAnalyticsRequest()
        response = Analytics.ExtensionAnalyticsResponse()
        await self.twitchAPICall(request, response)
        return response
    
    async def GetGameAnalytics(self, game_id: str, date_range: dateRange):
        request = Analytics.GameAnalyticsRequest(game_id, date_range)
        response = Analytics.GameAnalyticsResponse()
        await self.twitchAPICall(request, response)
        return response


    async def twitchAPICall(self, request: RequestBaseClass, response: ResponseBaseClase, **kwargs) -> None:
        #TODO: add in requirements checks 
        headers = {
            'Authorization': f'Bearer {self._access_token}',
            'Client-Id': self._client_id
        }
        APIjson = await self._APIRequest.getRequest(request.endPoint,headers=headers,kwargs=kwargs)
        APIresponse:dict = json.loads(APIjson)
        if APIresponse.get("error"):
             raise APIReqestFailedException(APIresponse)
        for key, value in APIresponse:
                response.__dict__[key] = value

    def getHeaders(self, requirements):
        return