#from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the albums index.")

def demo1(request):
    return HttpResponse("Hello, demo1!")