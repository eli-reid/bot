from typing import Any, Optional
from django.apps import AppConfig, apps
<<<<<<< HEAD
from .middleware import tci, StartTciClient

=======
from .middleware import  loadTCISettings
>>>>>>> 1d19cf16f809cb42948321cb312a34d0bb309588
class TciConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'TCI'
   
    def __init__(self, app_name: str, app_module: Optional[Any]) -> None:
        self.isConnected = tci.isConnected
        self.displayName = 'Chat Interface'
        self._settings:list[dict] =[
            {'key':'Server', 'value':'irc.chat.twitch.tv', 'readOnly':True, 'visible':True},
            {'key':'Port', 'value':'6667', 'readOnly':True, 'visible':True},
            {'key':'caprequest', 'value':'twitch.tv/tags twitch.tv/commands twitch.tv/membership', 'readOnly':True, 'visible':False},
            {'key':'User', 'value':'', 'readOnly':False, 'visible':True },
            {'key':'OAuth Key', 'value':'', 'readOnly':False, 'visible':True },
            {'key':'channels', 'value':'', 'readOnly':False, 'visible':True }
        ]
        super().__init__(app_name, app_module)

    def ready(self) -> None:
        self.settingsObj = apps.get_app_config('Home').get_model('Settings')
        self.load_default_settings()
<<<<<<< HEAD
        StartTciClient()
        return super().ready()

    def load_default_settings(self) -> None:
        for setting in self._settings:
            obj, created = self.settingsObj.objects.get_or_create(app=self.displayName, key=setting.get('key'), value=setting.get('value'), readOnly=setting.get('readOnly'), visible=setting.get('visible'))
            
    def reset_default_settings(self) -> None:
        for setting in self._settings:
            update = self.settingsObj.objects.get(app=self.displayName, key=setting.get('key'))
            update["value"] = setting.get('value')
            update.save()
=======
        loadTCISettings()
        return super().ready()

    def load_default_settings(self) -> None:
        try:
            for setting in self._settings:
                obj, created = self.settingsObj.objects.get_or_create(app=self.displayName, key=setting.get('key'), value=setting.get('value'), readOnly=setting.get('readOnly'), visible=setting.get('visible'))
        except:
            pass
    def reset_default_settings(self) -> None:
        try:
            for setting in self._settings:
                update = self.settingsObj.objects.get(app=self.displayName, key=setting.get('key'))
                update["value"] = setting.get('value')
                update.save()
        except:
            pass
>>>>>>> 1d19cf16f809cb42948321cb312a34d0bb309588
