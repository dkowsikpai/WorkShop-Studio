# chat/views.py
from django.shortcuts import render, HttpResponse
from django.utils.safestring import mark_safe
import json
from .models import *


def index(request):
    return render(request, 'chat/index.html', {})


def room(request, room_name):
    try:
        create = WorkShopCode.objects.get(heading=room_name)
        text = create.text
        return render(request, 'chat/room.html', {
            'room_name_json': mark_safe(json.dumps(room_name)),
            'init_data': text
        })
    except:
        create = WorkShopCode.objects.create(heading=room_name, text="", share=True)
        create.save()
        return render(request, 'chat/room.html', {
            'room_name_json': mark_safe(json.dumps(room_name))
        })


def database_submit(request):
    data = request.POST['data']
    room_name = request.POST['room_name']
    event = WorkShopCode.objects.get(heading=room_name)
    event.text = data
    event.save()
    return HttpResponse("Pushed")
