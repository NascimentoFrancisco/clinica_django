
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('clinic_app.urls.home_urls')),
    path('specialty/', include('clinic_app.urls.specialty_urls')),
    path('doctor/', include('clinic_app.urls.doctor_urls')),
    path('times/', include('clinic_app.urls.available_times')),
    path('schedule/', include('clinic_app.urls.medical_schedule_urls')),
    path('patient/', include('clinic_app.urls.patient_urls')),
    path('accounts/', include('clinic_app.urls.accounts_urls')),
    path('consultation/', include('clinic_app.urls.patient_consultation_urls')),
]
