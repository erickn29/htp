from django.urls import path
from . import views, cookies

urlpatterns = [
    path('', views.index, name='index'),
    path('documentation/', views.index, name='docs'),
    path('libraries/', views.index, name='libs'),
    path('cheatsheets/', views.index, name='cheatsheets'),
    path('interview/', views.index, name='interview'),
    path('forum/', views.index, name='forum'),
    path('set_cookie', cookies.set_cookie),
]

