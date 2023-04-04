# chat/routing.py
from django.conf.urls import url
from django.urls import path
from django.conf import settings

# from . import consumers
from chat import consumers

websocket_urlpatterns = [
    # url(r'^ws/chat/(?P<room_name>[^/]+)/$', consumers.ChatConsumer),
    # path('ws/chat/<str:room_name>/', consumers.AsyncChatConsumer2),
    # path("ws/opalmarket/trade-chat/<str:room_name>/", consumers.AsyncProductChatConsumer.as_asgi()),
    # path("ws/opalmarket/chat/profile/temp/", consumers.UserToUserChatConsumer.as_asgi()),
    # path("ws/opalmarket/trade-chat/room-list-info/<str:user_id>/",
    #      consumers.AsyncUserChattingRoomListManager.as_asgi()),
    # path("ws/opalmarket/trade-chat/v2/<str:room_name>/", consumers.AsyncProductChatConsumerVersion2.as_asgi()),
    # path("ws/opalmarket/trade-chat/room-list-info/v2/<str:user_id>/",
    #      consumers.AsyncUserChattingRoomListManagerVersion2.as_asgi()),
    path("ws/chat/<str:room_name>", consumers.ChatConsumer.as_asgi()),
]
