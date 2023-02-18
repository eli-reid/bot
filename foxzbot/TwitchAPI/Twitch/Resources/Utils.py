from dataclasses import dataclass, field
from datetime import datetime
@dataclass
class pagenation:
    cursor: str = field(default="")

@dataclass
class dateRange : 
        started_at: str = field(default="")
        ended_at: str = field(default="")

class RequestBaseClass:
      requestType: str
      scope: str
      requirements: str 
      endPoint: str

class ResponseBaseClase:
    
    def __init__(self) -> None:
         self._dataList: list
    
    @property
    def data(self):
          return self._dataList