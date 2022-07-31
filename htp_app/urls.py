from django.urls import path
from . import views, cookies

urlpatterns = [
    path('', views.index, name='index'),
    path('documentation/', views.documentation, name='docs'),
    path('libraries/', views.libraries, name='libs'),
    path('cheatsheets/', views.cheatsheets, name='cheatsheets'),
    path('interview/', views.interview, name='interview'),
    path('forum/', views.forum, name='forum'),
    path('set_cookie', cookies.set_cookie),
]

