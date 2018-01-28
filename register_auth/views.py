from django.contrib.auth import logout as logout_user, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.db import transaction
from django.shortcuts import render, redirect

from register_auth.forms import RegistrationForm
from register_auth.utils.decorators import is_auth_then_redirect_home
from user_profile.models import Profile


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


@transaction.atomic
def create_user(user_data):
    user, created = User.objects.get_or_create(username=user_data['username'],
                                               email=user_data['email'])
    if created:
        user.set_password(user_data['password1'])
        user.save()
    profile = Profile(user=user, avatar='system/default_avatar.png')
    profile.save()
    return user


@is_auth_then_redirect_home
def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = create_user(form.cleaned_data)
            # user = form.save()
            login(request, user)
            return redirect('/user/{}/'.format(user.id))
        else:
            return render(request, 'register_auth/registration.html', {
                'form': form,
            })
    elif request.method == 'GET':
        form = RegistrationForm()
        return render(request, 'register_auth/registration.html', {
            'form': form,
        })
