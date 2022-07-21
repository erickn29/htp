from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect


def index(request):
    if len(request.COOKIES) >= 7:
        theme = request.COOKIES['theme']
        code_theme = request.COOKIES['code_theme']
        burger = request.COOKIES['burger']
        toggler = request.COOKIES['toggler']
        map_ = request.COOKIES['map']
        like = request.COOKIES['like']
        up = request.COOKIES['up']
    else:
        theme = '/static/css/white.css'
        code_theme = '/static/css/hljs/default.min.css'
        burger = '/static/img/menu-burger-white.png'
        toggler = '/static/img/moon.png'
        map_ = '/static/img/map-white.png'
        like = '/static/img/social-white.png'
        up = '/static/img/angle-up-white.png'
    test = 'BLABLABLA'
    context = {
        'theme': theme,
        'code_theme': code_theme,
        'burger': burger,
        'toggler': toggler,
        'map': map_,
        'like': like,
        'up': up,
        'test': test
    }
    return render(request, 'htp_app/index.html', context=context)


def set_cookie(request):
    response = HttpResponse()
    theme = request.GET['theme']
    code_theme = request.GET['code_theme']
    burger = request.GET['burger']
    toggler = request.GET['toggler']
    map_ = request.GET['map']
    like = request.GET['like']
    up = request.GET['up']
    response.set_cookie('theme', theme)
    response.set_cookie('code_theme', code_theme)
    response.set_cookie('burger', burger)
    response.set_cookie('toggler', toggler)
    response.set_cookie('map', map_)
    response.set_cookie('like', like)
    response.set_cookie('up', up)
    return response
