from django.apps import AppConfig
from .middleware import websocketServer

class WebsockConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Websock'
    def __init__(self, app_name: str, app_module) -> None:
        self.broadcast = websocketServer.broadcast 
        super().__init__(app_name, app_module)
 

