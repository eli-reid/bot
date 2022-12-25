"""
WSGI config for foxzbot project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""
import asyncio
from threading import Thread
import os
from TCI.middleware import startTCI
from Websock.middleware import ws
from django.urls import resolve
from TwitchAPI.Twitch.oauth import twitchOauth
from django.core.wsgi import get_wsgi_application
def runner():
        loop = asyncio.events.new_event_loop()
        loop.create_task(ws())
        loop.run_forever()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'foxzbot.settings')
application = get_wsgi_application()
newthread = Thread(target=runner, daemon=True)
newthread.start()
startTCI()


