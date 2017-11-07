import json

from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def login(request):
    print(request.GET['email'])
    return render(request, 'index.html')


def register(request):
    return render(request, 'index.html')
