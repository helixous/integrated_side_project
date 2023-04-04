from django.conf import settings
from django.shortcuts import render

# Create your views here.


# chat/view.py
from django.shortcuts import render
from rest_framework.decorators import api_view


def lobby(request):
    return render(
        request, 'lobby.html', {}
    )


def room(request, room_name):
    print(request.headers)
    return render(
        request,
        'room.html',
        {
            'room_name': room_name,
            'debug': settings.DEBUG
        }
    )
