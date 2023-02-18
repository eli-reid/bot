"""
Get Extension Analytics

requset:

curl -X GET 'https://api.twitch.tv/helix/analytics/extensions' \
-H 'Authorization: Bearer cfabdegwdoklmawdzdo98xt2fo512y' \
-H 'Client-Id: uo6dggojyb8d6soh92zknwmi5ej1q2'

response:

{
   "data": [
      {
         "extension_id": "efgh",
         "URL": "https://twitch-piper-reports.s3-us-west-2.amazonaws.com/dynamic/LoL%20ADC...",
         "type": "overview_v2",
         "date_range": {
            "started_at": "2018-03-01T00:00:00Z",
            "ended_at": "2018-06-01T00:00:00Z"
         }
      },
      ...
   ],
   "pagination": {"cursor": "eyJiIjpudWxsLCJhIjp7Ik9mZnNldCI6NX19"}
}


"""
import Scope 
from Utils import dateRange, RequestBaseClass, ResponseBaseClase,pagenation

class ExtensionAnalyticsRequest(RequestBaseClass):
  requestType = "GET"
  scope = Scope.Analytics.Read.Extensions
  requirements = ["user access token"]
  endPoint = "/analytics/extensions"

class ExtensionAnalyticsItem():
    def __init__(self) -> None:
        self.extension_id:str
        self.URL:str
        self.type:str
        self._dateRange: dateRange

    @property    
    def date_range(self) -> dateRange:
       return self._dateRange
    
    @date_range.setter
    def date_range(self,daterange: dict[str,str]):
       for key, val in daterange:
          self._dateRange[key]=val

class ExtensionAnalyticsResponse(ResponseBaseClase):
    def __init__(self) -> None:
        self._paganation:pagenation
        super().__init__()
   
    @super().data.setter
    def data(self, dataItems:list):
        for key, value in dataItems:
            tmpItem = ExtensionAnalyticsItem()
            tmpItem.__dict__[key] = value
            self._dataList.append(tmpItem)
    
    @property
    def pagenation(self) -> pagenation:
        return self._paganation
    
    @pagenation.setter
    def pagenation(self, page: dict):
        self._paganation.cursor = page.get("cursor")
        
      


"""
Get Game Analytics

requset:
curl -X GET 'https://api.twitch.tv/helix/analytics/games?game_id=493057&started_at=2018-01-01T00:00:00Z&ended_at=2018-03-01T00:00:00Z' \
-H 'Authorization: Bearer cfabdegwdoklmawdzdo98xt2fo512y' \
-H 'Client-Id: uo6dggojyb8d6soh92zknwmi5ej1q2'

response:
{
  "data": [
    {
      "game_id" : "493057",
      "URL" : "https://twitch-piper-reports.s3-us-west-2.amazonaws.com/games/66170/overview/15183...",
      "type" : "overview_v2",
      "date_range" : {
        "started_at" : "2018-01-01T00:00:00Z",
        "ended_at" : "2018-03-01T00:00:00Z"
      }
    }
  ]
}

"""

class GameAnalyticsRequest(RequestBaseClass):
    requestType = "GET"
    scope = Scope.Analytics.Read.Extensions
    requirements = ["user access token"]
    endPoint = "/analytics/extensions"
    game_id: str
    date_range: dateRange
    def __init__(self, game_id: str, date_range: dateRange) -> None:
        self.game_id = game_id
        self.date_range = date_range
        super().__init__()

class GameAnalyticsItem():
    def __init__(self) -> None:
        self.game_id:str
        self.URL:str
        self.type:str
        self._dateRange: dateRange

    @property    
    def date_range(self) -> dateRange:
       return self._dateRange
    
    @date_range.setter
    def date_range(self,daterange: dict[str,str]):
       for key, val in daterange:
          self._dateRange[key]=val

class GameAnalyticsResponse(ResponseBaseClase):

    @super().data.setter
    def data(self, dataItems:list):
        for key, value in dataItems:
            tmpItem = GameAnalyticsItem()
            tmpItem.__dict__[key] = value
            self._dataList.append(tmpItem)