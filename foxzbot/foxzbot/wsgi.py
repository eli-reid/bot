"""
WSGI config for foxzbot project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""
import os
from TCI.middleware import StartTciClient
from Websock.middleware import StartWebsocketServer
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'foxzbot.settings')
application = get_wsgi_application()
StartWebsocketServer()
<<<<<<< HEAD
#StartTciClient()


=======
StartTciClient()
>>>>>>> 1d19cf16f809cb42948321cb312a34d0bb309588
