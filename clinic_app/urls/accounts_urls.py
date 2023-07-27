from django.urls import path
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from clinic_app.views.accounts_views import (
    LogoutUser, LoginUser, DeactivateUserView,
    ActivateUserView, DetailUserView, CreateUserAdminView,
    UpdateUserAdmin, ListUserAdmin
)

urlpatterns = [
    path("logout/", LogoutUser.as_view(), name="logout_user"),
    path("login/", LoginUser.as_view(), name="login_user"),
    path("create/", CreateUserAdminView.as_view(), name="create_user"),
    path("list/", ListUserAdmin.as_view(), name="list_user"),
    path('change-password/', auth_views.PasswordChangeView.as_view(
            template_name='accounts/change_password.html',
            success_url = reverse_lazy('home')
        ),
        name='change_password'
    ),
    path("update/<int:pk>/", UpdateUserAdmin.as_view(), name="update_user"),
    path("detail/<int:pk>/", DetailUserView.as_view(), name="detail_user"),
    path("deactivate/<int:pk>/", DeactivateUserView.as_view(), name="deactivate_user"),
    path("activate/<int:pk>/", ActivateUserView.as_view(), name="activate_user"),
]
