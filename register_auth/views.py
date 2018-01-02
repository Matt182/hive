from django.contrib.auth import logout as logout_user, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from register_auth.forms import RegistrationForm
from register_auth.utils.decorators import is_auth_then_redirect_home


@is_auth_then_redirect_home
def index(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/user/{}/'.format(user.id))
        return render(request, 'register_auth/index.html', {
            'form': form
        })
    elif request.method == 'GET':
        form = AuthenticationForm()
        return render(request, 'register_auth/index.html', {
            'form': form
        })


@login_required
def logout(request):
    logout_user(request)
    return redirect('/')


@is_auth_then_redirect_home
def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/user/')
        else:
            return render(request, 'register_auth/registration.html', {
                'form': form,
            })
    elif request.method == 'GET':
        form = RegistrationForm()
        return render(request, 'register_auth/registration.html', {
            'form': form,
        })
