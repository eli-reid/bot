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
from Utils import dateRange

class GetExtensionAnalyticsRequest():
  scope = Scope.Analytics.Read.Extensions
  requirements= ["user access token"]
  endPoint = "/analytics/extensions"

class GetExtensionAnalyticsReponseItem():
    extension_id:str
    URL:str
    type:str
    date_range: dateRange


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