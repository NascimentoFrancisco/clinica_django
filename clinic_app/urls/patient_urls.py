from django.urls import path
from clinic_app.views.patient_views import (
    CreatePatientUserView, DetailPatientView,
    UpdatePatientUserView, ListPatientView
)

urlpatterns = [
    path("create/", CreatePatientUserView.as_view(), name="create_patient_user"),
    path("list/", ListPatientView.as_view(), name="list_patient_user"),
    path("detail/", DetailPatientView.as_view(), name="detail_patient_user"),
    path("update/<int:pk>/", UpdatePatientUserView.as_view(), name="update_patient_user"),
]
