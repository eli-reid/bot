from Resources.Utils import pagenation, dateRange, RequestBaseClass, ResponseBaseClase
from Resources import Analytics, Ads
from ApiRequest import APIRequest
import json
from typing import Tuple
class APIReqestFailedException(Exception):
     pass

class twitchAPI:

    def __init__(self) -> None:
        self._APIRequest = APIRequest("https://api.twitch.tv/helix/")

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







    async def twitchAPICall(self, request: RequestBaseClass, response: ResponseBaseClase) -> None:
        #TODO: add in requirements checks 
        APIjson = await self._APIRequest.getRequest(request.endPoint)
        APIresponse:dict = json.loads(APIjson)
        if APIresponse.get("error"):
             raise APIReqestFailedException(APIresponse)
        for key, value in APIresponse:
                response.__dict__[key] = value
