from django.urls import path, include
from . import views

urlpatterns = [
    # 채팅방 테스트
    path('lobby', views.lobby),
    path('room/<str:room_name>', views.room),
]
