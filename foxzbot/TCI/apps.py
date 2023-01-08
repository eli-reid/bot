from typing import Any, Optional
from django.apps import AppConfig, apps
from django.db import models

class TciConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'TCI'
    
    def ready(self) -> None:
        self.displayName = 'Chat Interface'
        self.settingsObj = apps.get_app_config('Home').get_model('Settings')
        if self.settingsObj.objects.filter(app=self.displayName).count()<1:
            self.load_default_settings()
        return super().ready()

    def load_default_settings(self):
        records: list[models.Model] =[]
        records.append (self.settingsObj(app=self.displayName, key='Server', value='irc.chat.twitch.tv', readOnly = True))
        records.append (self.settingsObj(app=self.displayName, key='Port', value='6667', readOnly = True))
        records.append (self.settingsObj(app=self.displayName, key='caprequest', value='twitch.tv/tags twitch.tv/commands twitch.tv/membership', readOnly = True))
        records.append (self.settingsObj(app=self.displayName, key='User', value='', readOnly = False))
        records.append (self.settingsObj(app=self.displayName, key='OAuth Key', value='', readOnly = False))
        records.append (self.settingsObj(app=self.displayName, key='channels', value='', readOnly = False))
        for record in records:
            record.save()