
from django.apps import AppConfig, apps
from django.db import models
class TwitchapiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'TwitchAPI'

    def ready(self) -> None:
        self.displayName = 'Twitch API'
        self.settingsObj = apps.get_app_config('Home').get_model('Settings')
        if self.settingsObj.objects.filter(app=self.displayName).count()<1:
            self.load_default_settings()
        return super().ready()

    def load_default_settings(self):
        records: list[models.Model]=[]
        records.append (self.settingsObj(app=self.displayName, key='expires', value='', readOnly = True, visible = False))
        records.append (self.settingsObj(app=self.displayName, key='token_type', value='', readOnly = True, visible = False))
        records.append (self.settingsObj(app=self.displayName, key='access_token', value='', readOnly = True, visible = False))
        records.append (self.settingsObj(app=self.displayName, key='refresh_token', value='', readOnly = True, visible = False))
        records.append (self.settingsObj(app=self.displayName, key='scope', value='', readOnly = True, visible = False))
        for record in records:
            record.save()