from aiohttp import ClientResponse, http_exceptions
from .Resources.Utils import pagenation, dateRange, RequestBaseClass, ResponseBaseClass
from .Resources import Analytics, Ads, Bits
from .ApiRequest import APIRequest
from typing import Callable, Optional
class TwitchApiUnauthorizedException(Exception):
     pass
class TwitchApiBadRequstException(Exception):
     pass
class TwitchApiNotFoundException(Exception):
     pass
class TwitchApiTooManyRequestsException(Exception):
     pass

class twitchAPI:
    def __init__(self, client_id:str, client_credentials:str, access_token:str, user_id) -> None:
        self._APIRequest: APIRequest = APIRequest("https://api.twitch.tv/helix")
        self._client_id: str = client_id
        self._client_credentials: str =  client_credentials
        self._user_access_token: str = access_token
        self._user_id: str = user_id

    def getHeaders(self, requirements):
        return
    
    def getParams(self, request: RequestBaseClass) -> list[tuple]:
        params = list()
        for key, value in request.__dict__.items():
            if isinstance(value,list):
                for item in value:
                    params.append((key, item))
            else:
                params.append((key,value))
        return params

    def _RequestFunctionType(self, requestType: str) -> Callable:
        func = None
        if requestType == "DELETE":
            func = self._APIRequest.deleteRequest
        if requestType == "GET":
            func = self._APIRequest.getRequest        
        if requestType == "POST":
            func = self._APIRequest.postRequest
        if requestType == "PUT":
            func = self._APIRequest.putRequest    
        return func

    async def _APIReqestFailed(self, response: ClientResponse) -> Exception:
        exception = Exception
        if response.status == 400:
            exception = TwitchApiBadRequstException(await response.json())
        if response.status == 401:
            exception = TwitchApiUnauthorizedException(await response.json())
        if response.status == 404:
            exception = TwitchApiNotFoundException(await response.json())
        if response.status == 429:
            exception = TwitchApiTooManyRequestsException(await response.json())
        return exception    

    async def twitchAPICall(self, request: RequestBaseClass, response: ResponseBaseClass, **kwargs) -> None:
        """
        Raises APIReqestFailedException(APIresponse)
        """
        #TODO: add in requirements checks 
        headers = {
            'Authorization': f'Bearer {self._client_credentials}',
            'Client-Id': self._client_id
        }
        requestFunction = self._RequestFunctionType(request.requestType)
        APIresponse:ClientResponse = await requestFunction(request.endPoint, headers=headers, params=self.getParams(request), kwargs=kwargs)
        if APIresponse.status == 200:
            response.raw = await APIresponse.json()
            for key, value in response.raw.items():
                    response.__setattr__(key, value)
            return
        raise await self._APIReqestFailed(APIresponse)

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

    async def GetBitsLeaderboard(self, count:Optional[int] = 10, period: Optional[str] = "all", started_at: Optional[str] = "", user_id: Optional[str]= "") -> Bits.BitsLeaderboardResponse:
        request = Bits.BitsLeaderboardRequest(count, period, started_at, user_id)
        response = Bits.BitsLeaderboardResponse()
        await self.twitchAPICall(request, response)
        return response

    async def GetCheermotes(self, broadcaster_id: Optional[str] = None) -> Bits.CheermotesResponse:
        request = Bits.CheermotesRequest(broadcaster_id)
        response = Bits.CheermotesResponse()
        await self.twitchAPICall(request, response)
        return response

    async def GetExtensionTransactions(self, extension_id:str, id: Optional[str]=None, first: Optional[int]=None, after: Optional[str]=None) -> Bits.ExtensionTransactionsResponse:
        request = Bits.ExtensionTransactionsRequest(extension_id, id, first, after)
        response = Bits.ExtensionTransactionsResponse()
        await self.twitchAPICall(request, response)
        return response
