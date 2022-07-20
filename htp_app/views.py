from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect


def index(request):
    if request.COOKIES.get('theme'):
        theme = request.COOKIES['theme']
    else:
        theme = '/static/css/white.css'
    return render(request, 'htp_app/index.html', context={'theme': theme})


def set_cookie(request):
    response = HttpResponse()
    theme = request.GET['theme']
    response.set_cookie('theme', theme)
    return response

