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
from .import Scope 
from .Utils import dateRange, \
                DateRangeMixin,\
                RequestBaseClass,\
                ResponseBaseClass,\
                PagenationMixin

class ExtensionAnalyticsRequest(RequestBaseClass):
  requestType = "GET"
  scope = Scope.Analytics.Read.Extensions
  requirements = ["user access token"]
  endPoint = "/analytics/extensions"

class ExtensionAnalyticsItem(DateRangeMixin):
    def __init__(self) -> None:
        self.extension_id:str
        self.URL:str
        self.type:str

class ExtensionAnalyticsResponse(PagenationMixin, ResponseBaseClass):
    def __init__(self) -> None:
        super().__init__()

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

class GameAnalyticsItem(DateRangeMixin):
    def __init__(self) -> None:
        self.game_id:str
        self.URL:str
        self.type:str
        
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


class GameAnalyticsResponse(PagenationMixin, ResponseBaseClass):
    def __init__(self) -> None:
        super().__init__(GameAnalyticsItem)