import json

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render


def get_current_user(request):
    return request.user


@login_required
def index(request):
    user = get_current_user(request)
    return render(request, 'index.html', {
        'user': user,
    })


@login_required
def friends(request):
    user = get_current_user(request)
    user_friends = user.get_friends()
    return render(request, 'friends.html', {
        'user': user,
        'friends': user_friends,
    })


@login_required
def members(request):
    user = get_current_user(request)
    members = User.objects.all()
    return render(request, 'members.html', {
        'user': user,
        'members': members
    })
