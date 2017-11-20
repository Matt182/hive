from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from user_profile.helpers.friend_helpers import \
    get_friends, \
    get_relation_to, \
    send_friend_request as send_request, \
    accept_friend_request as accept_request, \
    decline_friend_request as decline_request, \
    delete_friend as delete_f


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
    status = get_relation_to(user.id, person_id)
    return render(request, 'user_profile/index.html', {
        'user': user,
        'person': person,
        'owner': False,
        'status': status,
    })


@login_required
def friends(request):
    user = get_current_user(request)
    user_friends = get_friends(user.id)
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
    user = get_current_user(request)
    send_request(user.id, person_id)
    return redirect('person', person_id=person_id)


@login_required
def accept_friend_request(request, person_id):
    user = get_current_user(request)
    accept_request(user.id, person_id)
    return redirect('person', person_id=person_id)


@login_required
def decline_received_friend_request(request, person_id):
    user = get_current_user(request)
    decline_request(user.id, person_id)
    return redirect('person', person_id=person_id)


@login_required
def decline_send_friend_request(request, person_id):
    user = get_current_user(request)
    decline_request(person_id, user.id)
    return redirect('person', person_id=person_id)


@login_required
def delete_friend(request, person_id):
    user = get_current_user(request)
    delete_f(user.id, person_id)
    return redirect('person', person_id=person_id)
