from django.urls import path, include
from . import views, cookies
from .views import *

urlpatterns = [
    path('', AllArticlesListView.as_view(), name='index'),
    path('documentation/', DocumentationListView.as_view(), name='docs'),
    path('libraries/', LibraryListView.as_view(), name='libs'),
    path('cheatsheets/', CheatsheetListView.as_view(), name='cheatsheets'),
    path('interview/', InterviewListView.as_view(), name='interview'),
    path('forum/', views.forum, name='forum'),
    path('<slug:category>/<slug:article>/', ArticleDetailView.as_view(), name='article'),
    path('set_cookie', cookies.set_cookie),

]

