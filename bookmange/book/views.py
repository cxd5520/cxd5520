from django.shortcuts import render

# Create your views here.

# request
from django.http import HttpResponse
from django.http import HttpRequest

def index(request):

    return HttpResponse('ojbk')
