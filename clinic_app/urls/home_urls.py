from django.urls import path
from clinic_app.views.home_view import HomeView

urlpatterns = [
    path("", HomeView.as_view(), name="home")
]
