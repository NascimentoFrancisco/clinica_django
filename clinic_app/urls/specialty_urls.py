from django.urls import path
from clinic_app.views.specialty_views import CreateSpecialtyView

urlpatterns = [
    path("create/", CreateSpecialtyView.as_view(), name="create_specialty")
]