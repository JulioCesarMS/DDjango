from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings
from core.urls import core_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(core_urlpatterns)),
    path('shop/', include(core_urlpatterns)),

]


urlpatterns += [
    path("ckeditor5/", include('django_ckeditor_5.urls')),
] 


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)