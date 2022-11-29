"""
ASGI config for foxzbot project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
uvicorn foxzbot.asgi:application --reload  
"""
import asyncio
import os
from django.core.asgi import get_asgi_application
from TCI.middleware import startTCI
from Websock.middleware import ws
from django.urls import resolve

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'foxzbot.settings')
application = get_asgi_application()

asyncio.create_task(ws(), name="task2")
startTCI()