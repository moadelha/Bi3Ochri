from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('car.urls')),
]

# Afixing the photos 
urlpatterns += staticfiles_urlpatterns() 

# Serve media files during development
if settings.DEBUG:  # Ensure this only runs in development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
