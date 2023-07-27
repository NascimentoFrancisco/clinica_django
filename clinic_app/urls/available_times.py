from django.urls import path
from clinic_app.views.available_times import(
    CreateAvailableTimesView, ListAvailableTimesView,
    UpdateAvailableTimesView, DeleteAvailableTimesView
)

urlpatterns = [
    path("create/", CreateAvailableTimesView.as_view(), name="create_available_times"),
    path("list/", ListAvailableTimesView.as_view(), name="list_available_times"),
    path("update/<int:pk>/", UpdateAvailableTimesView.as_view(), name="update_available_times"),
    path("delete/<int:pk>/", DeleteAvailableTimesView.as_view(), name="doctor_available_times"),
]
