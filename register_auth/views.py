from django.contrib.auth import authenticate, login as login_user, logout as logout_user
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from register_auth.utils.decorators import is_auth_then_redirect_home


@is_auth_then_redirect_home
def index(request):
    return render(request, 'register_auth/index.html')


@is_auth_then_redirect_home
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login_user(request, user)
        return redirect('/user/')
    return redirect('/')


@login_required
def logout(request):
    logout_user(request)
    return redirect('/')


@is_auth_then_redirect_home
def registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username=username, email=email, password=password)
        if user is not None:
            login_user(request, user)
            return redirect('/user/')
    elif request.method == 'GET':
        return render(request, 'register_auth/registration.html')
