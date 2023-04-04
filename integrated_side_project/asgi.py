"""
ASGI config for integrated_side_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application

from chat import routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "integrated_side_project.settings")

application = ProtocolTypeRouter(
    {
        # (http->django views is added by default)
        'http': get_asgi_application(),

        'websocket': AllowedHostsOriginValidator(
            AuthMiddlewareStack(
                URLRouter(
                    routing.websocket_urlpatterns
                )
            )
        ),
        # 'websocket': AuthMiddlewareStack(
        #     URLRouter(
        #         routing.websocket_urlpatterns
        #     )
        # ),
    }
)
