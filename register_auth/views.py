import json

from django.contrib.auth import authenticate, login as login_user
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'index.html')


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login_user(request, user)
        return redirect('/user/')
    return redirect('/')


def register(request):
    return render(request, 'index.html')
