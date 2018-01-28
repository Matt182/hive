from django.shortcuts import redirect


def is_auth_then_redirect_home(func=None):
    def func_wrapper(request):
        if request.user.is_authenticated:
            return redirect('/user/{}/'.format(request.user.id))
        else:
            return func(request)

    return func_wrapper
