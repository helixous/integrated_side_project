import json

import ujson
from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer

# class ChattingConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         ...
#
#     async def disconnect(self, code):
#         ...
#
#     async def receive(self, text_data=None, bytes_data=None):
#         ...
#
from core.utils import execution_time_checker


class ChatConsumer(AsyncWebsocketConsumer):
    @execution_time_checker
    async def connect(self):
        print('연결메서드 동작')
        print('스코프 정보 : ', self.scope)
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name, self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data=None, bytes_data=None):
        # print('넘어온 데이터(text, bytes 순)')
        # print(text_data)
        # print(bytes_data)
        text_data_json = ujson.loads(text_data)
        message = text_data_json["message"]

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat_message", "message": message}
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]
        # Send message to WebSocket
        await self.send(text_data=ujson.dumps({"message": message}))
