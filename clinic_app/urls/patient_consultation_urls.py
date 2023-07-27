from django.urls import path
from clinic_app.views.patient_consultation_views import (
    CreatePatientConsultationView, ListPatientConsultationView,
    DetailPatientConsultationView, DeletePatientConsultationView,
    ListPatientConsultationActiveView, ListAllPatientConsultationView,
    FinishPatientConsultationView
)

urlpatterns = [
    path("create/<int:pk>/", CreatePatientConsultationView.as_view(), name="create_patient_consultation"),
    path("list/", ListPatientConsultationView.as_view(), name="list_patient_consultation"),
    path("list-all/", ListAllPatientConsultationView.as_view(), name="list_patient_consultation_all"),
    path("list-active/", ListPatientConsultationActiveView.as_view(), name="list_patient_consultation_active"),
    path("finish/<int:pk>/", FinishPatientConsultationView.as_view(), name="finish_patient_consultation"),
    path("detail/<int:pk>/", DetailPatientConsultationView.as_view(), name="detail_patient_consultation"),
    path("delete/<int:pk>/", DeletePatientConsultationView.as_view(), name="doctor_patient_consultation"),
]
