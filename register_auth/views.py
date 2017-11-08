from django.contrib.auth import authenticate, login as login_user, logout as logout_user
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from register_auth.utils.decorators import is_auth


@is_auth
def index(request):
    print(request.user.is_authenticated)
    print('register_auth')
    return render(request, 'reg_index.html')


@is_auth
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

@is_auth
def register(request):
    return render(request, 'index.html')
