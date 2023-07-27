from django.urls import path
from clinic_app.views.doctor_views import (
    CreateDoctorView, UpdateDoctorView, ListdoctorView,
    DetailDoctorView, DeleteDoctorView
)

urlpatterns = [
    path("create/", CreateDoctorView.as_view(), name="create_doctor"),
    path("list/", ListdoctorView.as_view(), name="list_doctor"),
    path("update/<int:pk>/", UpdateDoctorView.as_view(), name="update_doctor"),
    path("detail/<int:pk>/", DetailDoctorView.as_view(), name="detail_doctor"),
    path("delete/<int:pk>/", DeleteDoctorView.as_view(), name="doctor_doctor"),
]
