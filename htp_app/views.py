from django.shortcuts import render
from django.shortcuts import redirect
from .cookies import cookie_to_template
from django.views import View


def index(request):
    context = {
        'test': 'index page'
    }
    cookies = cookie_to_template(request)
    context.update(cookies)
    return render(request, 'htp_app/index.html', context)


def documentation(request):
    context = {
        'test': 'doc page'
    }
    cookies = cookie_to_template(request)
    context.update(cookies)
    return render(request, 'htp_app/documentation.html', context)


def libraries(request):
    context = {
        'test': 'lib page'
    }
    cookies = cookie_to_template(request)
    context.update(cookies)
    return render(request, 'htp_app/libraries.html', context)


def cheatsheets(request):
    context = {
        'test': 'cheat page'
    }
    cookies = cookie_to_template(request)
    context.update(cookies)
    return render(request, 'htp_app/cheatsheets.html', context)


def interview(request):
    context = {
        'test': 'int page'
    }
    cookies = cookie_to_template(request)
    context.update(cookies)
    return render(request, 'htp_app/interview.html', context)


def forum(request):
    context = {
        'test': 'forum page'
    }
    cookies = cookie_to_template(request)
    context.update(cookies)
    return render(request, 'htp_app/forum.html', context)

