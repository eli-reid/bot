"""
Start Commercial

request:

curl -X POST 'https://api.twitch.tv/helix/channels/commercial' \
-H 'Authorization: Bearer 2gbdx6oar67tqtcmt49t3wpcgycthx' \
-H 'Client-Id: wbmytr93xzw8zbg0p1izqyzzc5mbiz' \
-H 'Content-Type: application/json' \
--data-raw '{
  "broadcaster_id": "41245072",
  "length": 60
}'

response:

{
  "data": [
    {
      "length" : 60,
      "message" : "",
      "retry_after" : 480
    }
  ]
}

"""
from dataclasses import dataclass, field
import Scope
from Utils import ResourceBaseClass,ResponseBaseClase

class StartCommercialRequest(ResourceBaseClass):
    requestType = "POST"
    scope = Scope.Channel.Edit.Commercial
    reqiurements = ["user access token"]
    endPoint = "/channels/commercial"
    broadcaster_id:str
    length:int

class StartCommercialItem():
    length: int
    message: str
    retry_after: int 

class StartCommercialRepsonse(ResponseBaseClase):
    @super().data.setter
    def data(self, dataItems:list):
        for key, value in dataItems:
            tmpItem = StartCommercialItem()
            tmpItem.__dict__[key] = value
            self._dataList.append(tmpItem)
    