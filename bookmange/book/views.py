from django.shortcuts import render

# Create your views here.

# request
from django.http import HttpResponse
from django.http import HttpRequest

def index(request):
    context = {
        'name': ' abc',
    }
    return render(request, 'book/index.html', context=context)
