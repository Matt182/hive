import json

from django.shortcuts import render
from .models import Profile


def get_current_user(request):
    return request.user


def index(request):
    user = get_current_user(request)
    return render(request, 'index.html', {
        'user': user,
    })


def friends(request):
    user = get_current_user(request)
    user_friends = Profile.objects.get(pk=user['id']).friends
    return render(request, 'friends.html', {
        'user': user,
        'friends': user_friends,
    })


def members(request):
    user = get_current_user(request)
    members = Profile.objects.all()
    return render(request, 'members.html', {
        'user': user,
        'members': members
    })
