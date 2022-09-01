from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from htp import settings

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('upravlenie_saitom/', admin.site.urls),
    path('', include('htp_app.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
