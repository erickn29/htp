from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('upravlenie_saitom/', admin.site.urls),
    path('', include('htp_app.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
