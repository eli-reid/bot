from typing import Any, Optional
from django.apps import AppConfig, apps
from django.db import models
class StreamtimerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'StreamTimer'

    def __init__(self, app_name: str, app_module: Optional[Any]) -> None:
        self._settings:list[dict] =[ 
            {'key':'time', 'value':'11:30', 'readOnly':False, 'visible':True },
            {'key':'DisplayMsg', 'value':'Stream Ending: ', 'readOnly':False, 'visible':True },
            {'key':'EndMsg', 'value':'Bed Time!', 'readOnly':False, 'visible':True },
            ]
        super().__init__(app_name, app_module)

    def ready(self) -> None:
        self.displayName = 'Stream Timer'
        self.settingsObj = apps.get_app_config('Home').get_model('Settings')
        self.load_default_settings()
        return super().ready()

    def load_default_settings(self):
        for setting in self._settings:
            obj, created = self.settingsObj.objects.get_or_create(app=self.displayName, key=setting.get('key'), value=setting.get('value'), readOnly=setting.get('readOnly'), visible=setting.get('visible'))
            
    def reset_default_settings(self):
        for setting in self._settings:
            update = self.settingsObj.objects.get(app=self.displayName, key=setting.get('key'))
            update["value"] = setting.get('value')
            update.save()
                      