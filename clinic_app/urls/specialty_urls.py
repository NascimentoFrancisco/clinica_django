from django.urls import path
from clinic_app.views.specialty_views import (
    CreateSpecialtyView, UpdateSpecialtyView,
    ListSpecialtyView, DeleteSpecialtyView
)

urlpatterns = [
    path("create/", CreateSpecialtyView.as_view(), name="create_specialty"),
    path("list/", ListSpecialtyView.as_view(), name="list_specialty"),
    path("update/<int:pk>/", UpdateSpecialtyView.as_view(), name="update_specialty"),
    path("delete/<int:pk>/", DeleteSpecialtyView.as_view(), name="delete_specialty"),
]