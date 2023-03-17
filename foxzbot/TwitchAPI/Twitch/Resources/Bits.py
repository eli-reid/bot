"""
Get Bits Leaderboard

requset:

curl -X GET 'https://api.twitch.tv/helix/bits/leaderboard?count=2&period=week&started_at=2018-02-05T08%3A00%3A00Z' \
-H 'Authorization: Bearer 2gbdx6oar67tqtcmt49t3wpcgycthx' \
-H 'Client-Id: uo6dggojyb8d6soh92zknwmi5ej1q2'

response

{
  "data": [
    {
      "user_id": "158010205",
      "user_login": "tundracowboy",
      "user_name": "TundraCowboy",
      "rank": 1,
      "score": 12543
    },
    {
      "user_id": "7168163",
      "user_login": "topramens",
      "user_name": "Topramens",
      "rank": 2,
      "score": 6900
    }
  ],
  "date_range": {
    "started_at": "2018-02-05T08:00:00Z",
    "ended_at": "2018-02-12T08:00:00Z"
  },
  "total": 2
}
"""
from . import Utils
from . import Scope 
from typing import Optional
class BitsLeaderboardRequest(Utils.RequestBaseClass):
    requestType = "GET"
    scope = Scope.Bits.Read
    requirements = ["user access token"]
    endPoint = "/bits/leaderboard"
    def __init__(self, count: Optional[int]=10, period: Optional[str]="all", 
                 started_at: Optional[str]=None, user_id: Optional[str]=None) -> None:
        self.count: int = count
        self.period: str = period
        self.started_at: str = started_at
        self.user_id: str = user_id
        super().__init__()

class BitsLeaderboardItem:
    def __init__(self) -> None:
        self.user_id:str = ""
        self.user_login:str = ""
        self.user_name:str = ""
        self.rank: int = -1
        self.score: int = -1

class BitsLeaderboardResponse(Utils.DateRangeMixin,Utils.ResponseBaseClass):
    def __init__(self) -> None:
        super().__init__(BitsLeaderboardItem)
   


"""
Get Cheermotes

requset:

curl -X GET 'https://api.twitch.tv/helix/bits/cheermotes?broadcaster_id=41245072' \
-H 'Authorization: Bearer 2gbdx6oar67tqtcmt49t3wpcgycthx' \
-H 'Client-Id: wbmytr93xzw8zbg0p1izqyzzc5mbiz'

response:

{
  "data": [
    {
      "prefix": "Cheer",
      "tiers": [
        {
            "min_bits": 1,
            "id": "1",
            "color": "#979797",
            "images": {
                "dark": {
                    "animated": {
                        "1": "https://d3aqoihi2n8ty8.cloudfront.net/actions/cheer/dark/animated/1/1.gif",
                        "1.5": "https://d3aqoihi2n8ty8.cloudfront.net/actions/cheer/dark/animated/1/1.5.gif",
                        "2": "https://d3aqoihi2n8ty8.cloudfront.net/actions/cheer/dark/animated/1/2.gif",
                        "3": "https://d3aqoihi2n8ty8.cloudfront.net/actions/cheer/dark/animated/1/3.gif",
                        "4": "https://d3aqoihi2n8ty8.cloudfront.net/actions/cheer/dark/animated/1/4.gif"
                    },
                    "static": {
                        "1": "https://d3aqoihi2n8ty8.cloudfront.net/actions/cheer/dark/static/1/1.png",
                        "1.5": "https://d3aqoihi2n8ty8.cloudfront.net/actions/cheer/dark/static/1/1.5.png",
                        "2": "https://d3aqoihi2n8ty8.cloudfront.net/actions/cheer/dark/static/1/2.png",
                        "3": "https://d3aqoihi2n8ty8.cloudfront.net/actions/cheer/dark/static/1/3.png",
                        "4": "https://d3aqoihi2n8ty8.cloudfront.net/actions/cheer/dark/static/1/4.png"
                        }
                },
                "light": {
                    "animated": {
                        "1": "https://d3aqoihi2n8ty8.cloudfront.net/actions/cheer/light/animated/1/1.gif",
                        "1.5": "https://d3aqoihi2n8ty8.cloudfront.net/actions/cheer/light/animated/1/1.5.gif",
                        "2": "https://d3aqoihi2n8ty8.cloudfront.net/actions/cheer/light/animated/1/2.gif",
                        "3": "https://d3aqoihi2n8ty8.cloudfront.net/actions/cheer/light/animated/1/3.gif",
                        "4": "https://d3aqoihi2n8ty8.cloudfront.net/actions/cheer/light/animated/1/4.gif"
                    },
                    "static": {
                        "1": "https://d3aqoihi2n8ty8.cloudfront.net/actions/cheer/light/static/1/1.png",
                        "1.5": "https://d3aqoihi2n8ty8.cloudfront.net/actions/cheer/light/static/1/1.5.png",
                        "2": "https://d3aqoihi2n8ty8.cloudfront.net/actions/cheer/light/static/1/2.png",
                        "3": "https://d3aqoihi2n8ty8.cloudfront.net/actions/cheer/light/static/1/3.png",
                        "4": "https://d3aqoihi2n8ty8.cloudfront.net/actions/cheer/light/static/1/4.png"
                    }
                }
            },
            "can_cheer": true,
            "show_in_bits_card": true
        }
        ...
      ],
      "type": "global_first_party",
      "order": 1,
      "last_updated": "2018-05-22T00:06:04Z",
      "is_charitable": false
    },
    ...
  ]
}
"""
class CheermotesRequest(Utils.RequestBaseClass):
    requestType = "GET"
    scope = None
    requirements = ["app access token","user access token"]
    endPoint = "/bits/cheermotes"
    def __init__(self,broadcaster_id:Optional[str] = None) -> None:
        self.broadcaster_id: Optional[str] = broadcaster_id
        super().__init__()

class ImageItem:
    animated : dict[str,str] = []
    static: dict[str,str] = []

class ImagesItem:
    dark: ImageItem = None
    light: ImageItem = None

class teirItem:
    min_bits: int = -1
    id: str = ""
    color: str = ""
    images: ImagesItem = None
    can_cheer: bool = False
    show_in_bits_card: bool =  False

class CheermotesItem:
  
    prefix: str = ""
    _tiers: list[teirItem] = list()
    type: str = ""
    order: int = -1
    last_updated: str = ""
    is_charitable: bool = False
    
    @property
    def tiers(self)->list[teirItem]:
        return self._tiers
    
    @tiers.setter
    def tiers(self,tiersList) -> None:
        for item in tiersList:
            tmpItem = teirItem()
            for key, value in item.items():
                tmpItem.__setattr__(key,value)
            self._tiers.append(tmpItem)



    
class CheermotesResponse(Utils.ResponseBaseClass):
    def __init__(self,) -> None:
        super().__init__(CheermotesItem)

"""
Get Extension Transactions

request:

curl -X GET
'https://api.twitch.tv/helix/extensions/transactions?extension_id=1234' \
-H 'Authorization: Bearer cfabdegwdoklmawdzdo98xt2fo512y' \
-H 'Client-Id: uo6dggojyb8d6soh92zknwmi5ej1q2'

response

{
  "data": [
    {
      "id": "74c52265-e214-48a6-91b9-23b6014e8041",
      "timestamp": "2019-01-28T04:15:53.325Z",
      "broadcaster_id": "439964613",
      "broadcaster_login": "chikuseuma",
      "broadcaster_name": "chikuseuma",
      "user_id": "424596340",
      "user_login": "quotrok",
      "user_name": "quotrok",
      "product_type": "BITS_IN_EXTENSION",
      "product_data": {
        "domain": "twitch.ext.uo6dggojyb8d6soh92zknwmi5ej1q2",
        "sku": "testSku100",
        "cost": {
          "amount": 100,
          "type": "bits"
        },
        "inDevelopment": false,
        "displayName": "Test Product 100",
        "expiration": "",
        "broadcast": false
      }
    },
    {
      "id": "8d303dc6-a460-4945-9f48-59c31d6735cb",
      "timestamp": "2019-01-18T09:10:13.397Z",
      "broadcaster_id": "439964613",
      "broadcaster_login": "chikuseuma",
      "broadcaster_name": "chikuseuma",
      "user_id": "439966926",
      "user_login": "liscuit",
      "user_name": "liscuit",
      "product_type": "BITS_IN_EXTENSION",
      "product_data": {
        "domain": "twitch.ext.uo6dggojyb8d6soh92zknwmi5ej1q2",
        "sku": "testSku200",
        "cost": {
          "amount": 200,
          "type": "bits"
        },
        "inDevelopment": false,
        "displayName": "Test Product 200",
        "expiration": "",
        "broadcast": false
      }
    },
    ...
  ],
  "pagination": {
    "cursor": "cursorString"
  }
}
"""

class ExtensionTransactionsRequest(Utils.RequestBaseClass):
    requestType = "GET"
    scope = None
    requirements = ["app access token"]
    endPoint = "/extensions/transactions"

    def __init__(self,extension_id: str, id: Optional[str]=None, first: Optional[int]=None, after: Optional[str] = None) -> None:
        self.extension_id: str = extension_id
        self.id: Optional[str] = id 
        self.first: Optional[int] = first
        self.after: Optional[str] = after
        super().__init__()

class ProductDataItem:
    domain: str = ""
    sku: str =""
    inDevelopment: bool = False,
    displayName: str = ""
    expiration:str = ""
    broadcast:bool = False   
    class cost: 
        amount: int = 0
        type: str = ""
     


class ExtensionTransactionItem:
    id: str = "",
    timestamp: str = ""
    broadcaster_id: str = ""
    broadcaster_login: str = ""
    broadcaster_name: str = ""
    user_id: str = ""
    user_login: str = ""
    user_name: str = ""
    product_type: str = ""
    product_data: ProductDataItem 

class ExtensionTransactionsResponse(Utils.PagenationMixin, Utils.ResponseBaseClass):
    def __init__(self) -> None:
        super().__init__(ExtensionTransactionItem)