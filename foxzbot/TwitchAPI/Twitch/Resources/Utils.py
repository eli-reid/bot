from dataclasses import dataclass, field
from datetime import datetime
@dataclass
class pagenation:
    cursor: str = field(default="")

@dataclass
class dateRange : 
        started_at: str = field(default="")
        ended_at: str = field(default="")

class DateRangeMixin:
    _dateRange:dateRange = dateRange()

    @property    
    def date_range(self) -> dateRange:
       return self._dateRange
    
    @date_range.setter
    def date_range(self,daterange: dict[str,str]):
       for key, val in daterange.items():
          self._dateRange.__setattr__(key,val)

class PagenationMixin:
    _paganation:pagenation = pagenation()

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

class ResponseBaseClass:
    dataitemtype =None
    def __init__(self, dataItem:object) -> None:
        self.raw: str = None
        self._dataItem = dataItem
        self.dataitemtype = dataItem 
        self._dataList: list[self._dataItem] = []

    @property
    def data(self) -> list[dataitemtype]:
          return self._dataList
    
    @data.setter
    def data(self, dataItems:list) -> None:
    
        for item in dataItems:
            tmpItem = self._dataItem()
            for key, value in item.items():
                tmpItem.__setattr__(key,value)
            self._dataList.append(tmpItem)