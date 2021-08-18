"""
ASGI config for myproject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
import django
from channels.http import AsgiHandler
from channels.routing import ProtocolTypeRouter
from myapp.consumers import SockConsumer
from channels.security.websocket import AllowedHostsOriginValidator
from django.urls import path, re_path
from channels.routing import ProtocolTypeRouter, URLRouter

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# application = get_asgi_application()

# django.setup()

application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": AllowedHostsOriginValidator(
        URLRouter([
                path(r'ws', SockConsumer.as_asgi()),
            ])
        
    )
  ## IMPORTANT::Just HTTP for now. (We can add other protocols later.)
})