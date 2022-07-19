from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('set_cookie',views.set_cookie),
]

