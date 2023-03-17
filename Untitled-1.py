
from typing import Optional
from dataclasses import dataclass, field
from datetime import datetime 
import json
@dataclass
class pagenation:
    cursor: str = field(default="")


class dateRange : 
    def __init__(self) -> None:
        self.started_at: str = ""
        self.ended_at: str = ""

class DateRangeBaseClass:
    _dateRange:dateRange = dateRange()

    @property    
    def date_range(self) -> dateRange:
       return self._dateRange
    
    @date_range.setter
    def date_range(self,daterange: dict[str,str]):
       for key, val in daterange.items():
          self._dateRange.__setattr__(key,val)


class PagenationBaseClass:
    def __init__(self) -> None:
        self._paganation:pagenation
    
    
    @property
    def pagenation(self) -> pagenation:
        return self._paganation
    
    @pagenation.setter
    def pagenation(self, page: dict):
        self._paganation.cursor = page.get("cursor")
        
class RequestBaseClass:
      requestType: str
      scope: str
      requirements: str 
      endPoint: str

class ResponseBaseClase:
    def __init__(self, dataItem:object) -> None:
         self._dataItem: object = dataItem 
         self._dataList: list = []

    @property
    def data(self):
          return self._dataList
    
    @data.setter
    def data(self, dataItems:list):
        for item in dataItems:
            tmpItem = self._dataItem()
            for key, value in item.items():
                tmpItem.__setattr__(key,value)
            self._dataList.append(tmpItem)
@dataclass
class BitsLeaderboardItem:
    def __init__(self) -> None:
        self.user_id:str
        self.user_login:str
        self.user_name:str
        self.rank:str
        self.score:str

class BitsLeaderboardResponse(DateRangeBaseClass,ResponseBaseClase):
    def __init__(self) -> None:
      
        self.total:int = 0
        super().__init__(BitsLeaderboardItem)


def twitchAPICall( request:str, response:ResponseBaseClase ) -> None:
        APIresponse:dict = json.loads(request)
        for key, value in APIresponse.items():
                response.__setattr__(key,value)


data = '''
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
'''
test = BitsLeaderboardResponse()
twitchAPICall(data, test )
test.data = json.loads(data)["data"]

print (test.total)
print(test.date_range.started_at)
print(test.date_range.ended_at)