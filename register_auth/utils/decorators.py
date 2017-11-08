from django.shortcuts import redirect


def is_auth(func=None):
    def func_wrapper(request):
        if request.user.is_authenticated:
            return redirect('/user/')
        else:
            return func(request)

    return func_wrapper
