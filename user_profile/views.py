from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from user_profile.forms import ProfileForm, create_populated_profile_form
from user_profile.helpers.friend_helpers import \
    get_friends, \
    get_relation_to, \
    send_friend_request as send_request, \
    accept_friend_request as accept_request, \
    decline_friend_request as decline_request, \
    delete_friend as delete_f
from user_profile.helpers.post_helpers import create_post
from user_profile.models import REQUEST_SEND, FRIEND, UNRELATED, Post


def get_current_user(request):
    return request.user


@login_required
def index(request):
    user = get_current_user(request)
    try:
        profile = user.profile
    except:
        profile = None
    posts = Post.objects.filter(owner_id=user.id).order_by('-created_at')

    return render(request, 'user_profile/index.html', {
        'user': user,
        'person': user,
        'owner': True,
        'profile': profile,
        'posts': posts
    })


@login_required
def person(request, person_id):
    user = get_current_user(request)
    if user.id == int(person_id):
        return redirect('profile')
    person = get_object_or_404(User, pk=person_id)
    try:
        profile = person.profile
    except:
        profile = None
    status = get_relation_to(user.id, person_id)
    posts = Post.objects.filter(owner_id=person.id).order_by('-created_at')

    return render(request, 'user_profile/index.html', {
        'user': user,
        'person': person,
        'owner': False,
        'status': status,
        'profile': profile,
        'posts': posts
    })


@login_required
def friends(request):
    user = get_current_user(request)
    user_friends = get_friends(user.id)
    print(user_friends)
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
@require_POST
def send_friend_request(request):
    user = get_current_user(request)
    person_id = request.POST['person_id']
    send_request(user.id, person_id)

    return JsonResponse({
        'result': 'success',
        'status': REQUEST_SEND,
    })


@login_required
@require_POST
def accept_friend_request(request):
    user = get_current_user(request)
    person_id = request.POST['person_id']
    accept_request(user.id, person_id)

    return JsonResponse({
        'result': 'success',
        'status': FRIEND,
    })


@login_required
@require_POST
def decline_received_friend_request(request):
    user = get_current_user(request)
    person_id = request.POST['person_id']
    decline_request(user.id, person_id)

    return JsonResponse({
        'result': 'success',
        'status': UNRELATED,
    })


@login_required
@require_POST
def decline_send_friend_request(request):
    user = get_current_user(request)
    person_id = request.POST['person_id']
    decline_request(person_id, user.id)

    return JsonResponse({
        'result': 'success',
        'status': UNRELATED,
    })


@login_required
@require_POST
def delete_friend(request):
    user = get_current_user(request)
    person_id = request.POST['person_id']
    delete_f(user.id, person_id)

    return JsonResponse({
        'result': 'success',
        'status': UNRELATED,
    })


@login_required
def add_profile_info(request):
    user = get_current_user(request)
    if request.method == 'POST':
        try:
            profile = user.profile
        except:
            profile = None
        form = ProfileForm(instance=profile, data=request.POST, files=request.FILES)

        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            return render(request, 'user_profile/profile_info_form.html', {
                'user': user,
                'form': form,
            })
    elif request.method == 'GET':
        form = create_populated_profile_form(user)

        return render(request, 'user_profile/profile_info_form.html', {
            'user': user,
            'form': form,
        })


@login_required
@require_POST
def send_post(request):
    user = get_current_user(request)
    owner_id = request.POST['wall_owner_id']
    msg = request.POST['message']
    post = create_post(owner_id, user.id, msg)
    data = serializers.serialize('json', [post], fields=('owner_id', 'author_id', 'created_at'))
    return JsonResponse({
        'result': 'success',
        'post': data,
    })
