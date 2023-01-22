from typing import Any, Optional
from django.apps import AppConfig, apps

class TwitchapiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'TwitchAPI'

    def __init__(self, app_name: str, app_module: Optional[Any]) -> None:
        self.displayName = 'Twitch API'
        self._settings:list[dict] =[
            {'key':'expires', 'value':'', 'readOnly':False, 'visible':False},
            {'key':'token_type', 'value':'', 'readOnly':False, 'visible':False},
            {'key':'access_token', 'value':'', 'readOnly':False, 'visible':False},
            {'key':'refresh_token', 'value':'', 'readOnly':False, 'visible':False},
            {'key':'scope', 'value':'', 'readOnly':False, 'visible':False}
        ]
        super().__init__(app_name, app_module)

    def ready(self) -> None:
        self.settingsObj = apps.get_app_config('Home').get_model('Settings')
        self.load_default_settings()
        return super().ready()

    def load_default_settings(self):
        try:
            for setting in self._settings:
                obj, created = self.settingsObj.objects.get_or_create(app=self.displayName, key=setting.get('key'), value=setting.get('value'), readOnly=setting.get('readOnly'), visible=setting.get('visible'))
        except:
            pass       
    def reset_default_settings(self):
        try:
            for setting in self._settings:
                update = self.settingsObj.objects.get(app=self.displayName, key=setting.get('key'))
                update["value"] = setting.get('value')
                update.save()
        except:
            pass
