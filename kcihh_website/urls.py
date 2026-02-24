"""
URL configuration for kcihh_website project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('about/', include('about.urls')),
    path('our-work/', include('our_work.urls')),
    path('impact/', include('impact.urls')),
    path('get-involved/', include('get_involved.urls')),
    path('resources/', include('resources.urls')),
    path('blog/', include('blog.urls')),
    path('contact/', include('contact.urls')),
    path('users/', include('users.urls')),
    path('tinymce/', include('tinymce.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)