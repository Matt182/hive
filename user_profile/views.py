import json

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404


def get_current_user(request):
    return request.user


@login_required
def index(request):
    user = get_current_user(request)
    return render(request, 'user_profile/index.html', {
        'user': user,
        'person': user,
        'owner': True,
    })


@login_required
def person(request, person_id):
    user = get_current_user(request)
    if user.id == int(person_id):
        return redirect('profile')
    person = get_object_or_404(User, pk=person_id)
    return render(request, 'user_profile/index.html', {
        'user': user,
        'person': person,
        'owner': False,
    })


@login_required
def friends(request):
    user = get_current_user(request)
    user_friends = user.get_friends()
    return render(request, 'user_profile/friends.html', {
        'user': user,
        'friends': user_friends,
    })


@login_required
def members(request):
    user = get_current_user(request)
    members = User.objects.all()
    return render(request, 'user_profile/members.html', {
        'user': user,
        'members': members
    })


@login_required
def send_friend_request(request, person_id):
    pass


@login_required
def accept_friend_request(request, person_id):
    pass


@login_required
def decline_friend_request(request, person_id):
    pass
