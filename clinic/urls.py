
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('clinic_app.urls.home_urls')),
    path('specialty/', include('clinic_app.urls.specialty_urls')),
]
