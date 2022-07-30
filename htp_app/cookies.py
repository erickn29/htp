from django.http import HttpResponse


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


def cookie_to_template(req):
    if len(req.COOKIES) >= 7:
        theme = req.COOKIES['theme']
        code_theme = req.COOKIES['code_theme']
        burger = req.COOKIES['burger']
        toggler = req.COOKIES['toggler']
        map_ = req.COOKIES['map']
        like = req.COOKIES['like']
        up = req.COOKIES['up']
    else:
        theme = '/static/css/white.css'
        code_theme = '/static/css/hljs/default.min.css'
        burger = '/static/img/menu-burger-white.png'
        toggler = '/static/img/moon.png'
        map_ = '/static/img/map-white.png'
        like = '/static/img/social-white.png'
        up = '/static/img/angle-up-white.png'
    context = {
        'theme': theme,
        'code_theme': code_theme,
        'burger': burger,
        'toggler': toggler,
        'map': map_,
        'like': like,
        'up': up,
    }
    return context
