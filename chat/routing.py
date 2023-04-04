# chat/routing.py
from django.urls import path
from django.conf import settings

# from . import consumers
from chat import consumers

websocket_urlpatterns = [
    path("ws/chat/<str:room_name>", consumers.ChatConsumer.as_asgi()),
]
