from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Menghubungkan URL utama ke aplikasi store kita
    path('', include('store.urls')), 
]

# Konfigurasi agar gambar bisa muncul saat mode Debug/Development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)