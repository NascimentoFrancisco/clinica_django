from django.urls import path
from clinic_app.views.medical_schedule_views import (
    CreateMedicalScheduleView, ListMedicalScheduleView, DetailMedicalScheduleView,
    UpdateMedicalScheduleView, DeleteMedicalScheduleView, ListMedicalScheduleForPatientView
)

urlpatterns = [
    path("create/", CreateMedicalScheduleView.as_view(), name="create_medical_schedule"),
    path("list/", ListMedicalScheduleView.as_view(), name="list_medical_schedule"),
    path("list-available/<int:pk>/", ListMedicalScheduleForPatientView.as_view(), 
        name="list_medical_schedule_available"
    ),
    path("update/<int:pk>/", UpdateMedicalScheduleView.as_view(), name="update_medical_schedule"),
    path("detail/<int:pk>/", DetailMedicalScheduleView.as_view(), name="detail_medical_schedule"),
    path("delete/<int:pk>/", DeleteMedicalScheduleView.as_view(), name="doctor_medical_schedule"),
]
