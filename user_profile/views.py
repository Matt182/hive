import json

from django.forms import model_to_dict
from django.shortcuts import get_object_or_404, render
from .models import User


def handle_s(request, id):
    user = model_to_dict(get_object_or_404(User, pk=id))
    request.session['user'] = json.dumps(user)


def get_current_user(request):
    return json.loads(request.session['user'])


def index(request):
    user = get_current_user(request)
    return render(request, 'index.html', {
        'user': user,
    })


def friends(request):
    user = get_current_user(request)
    user_friends = User.objects.get(pk=user['id']).friends
    return render(request, 'friends.html', {
        'user': user,
        'friends': user_friends,
    })


def members(request):
    user = get_current_user(request)
    members = User.objects.all()
    return render(request, 'members.html', {
        'user': user,
        'members': members
    })
