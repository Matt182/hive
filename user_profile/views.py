from django.http import HttpResponse
from .models import User


def index(request, id):
    user = User.
    return HttpResponse("Hello, world. You're at the polls index. user id is %s !!!" % user.name)