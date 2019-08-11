from django.shortcuts import render
from .models import *

# Create your views here.


def home(request):
    data = File.objects.filter(display=True).order_by('-upload_date')
    return render(request, 'dloader/home.html', {'data': data})
