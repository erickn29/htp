from django.shortcuts import render
from django.shortcuts import redirect
from .cookies import cookie_to_template


def index(request):
    context = {
        'test': 'test message'
    }
    cookies = cookie_to_template(request)
    context.update(cookies)
    return render(request, 'htp_app/index.html', context=context)
