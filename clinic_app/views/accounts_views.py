from typing import Any
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib import messages
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, UpdateView, DetailView, ListView
)
from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin
)
from django.contrib import messages
from django.shortcuts import redirect

from clinic_app.models.accounts import User
from clinic_app.forms.user_form import (
    CreationUserAdminForm, UpdateUserAdminForm
)


class TestMixinIsAdmin(UserPassesTestMixin):
    
    def test_func(self):
        is_superuser_or_is_staff = self.request.user.is_superuser or \
            self.request.user.is_staff
        return bool(is_superuser_or_is_staff)

    def handle_no_permission(self):
        messages.warning(
            self.request, "Você não tem autorização para essa página!"
        )
        return redirect("home")


class CreateUserAdminView(LoginRequiredMixin, TestMixinIsAdmin, CreateView):

    model = User
    template_name = 'accounts/create.html'
    form_class = CreationUserAdminForm
    success_url = reverse_lazy('list_user')

    def get_success_url(self) -> str:
        messages.success(
            self.request, 'Administrador cadastraddo com sucesso!'
        )
        return super().get_success_url()


class ListUserAdmin(LoginRequiredMixin, TestMixinIsAdmin, ListView):

    model = User
    template_name = 'accounts/list.html'
    paginate_by = 4

    def get_queryset(self) -> QuerySet[Any]:
        queryset = User.objects.filter(is_superuser=True)
        return queryset

class UpdateUserAdmin(LoginRequiredMixin, TestMixinIsAdmin, UpdateView):

    model = User
    template_name = 'accounts/create.html'
    form_class = UpdateUserAdminForm
    success_url = reverse_lazy('list_user')

    def get_success_url(self) -> str:
        messages.success(
            self.request, 'Administrador alterado com sucesso!'
        )
        return super().get_success_url()


class LoginUser(LoginView):

    template_name = 'accounts/login.html'

    def form_valid(self, form):
        messages.success(self.request, f'Bem vindo {form.get_user()}')
        return super().form_valid(form)
    

class LogoutUser(LogoutView):
    
    template_name = 'home/home.html'

    def get_success_url_allowed_hosts(self):
        messages.info(self.request,'Até breve!')
        return super().get_success_url_allowed_hosts()


class ActivateUserView(LoginRequiredMixin, TestMixinIsAdmin, UpdateView):

    model = User
    template_name = 'accounts/deactivate.html'
    fields = []
    success_url = reverse_lazy('list_patient_user')

    def form_valid(self, form):
        form.instance.is_active = True
        form.save()
        messages.success(self.request, 
            f'{self.get_object().name} ativado com sucesso!'
        )
        return super().form_valid(form)
    

class DeactivateUserView(LoginRequiredMixin, UpdateView):

    model = User
    template_name = 'accounts/deactivate.html'
    fields = []
    success_url = reverse_lazy('list_patient_user')

    def form_valid(self, form: BaseModelForm):
        form.instance.is_active = False
        form.save()
        messages.success(self.request, 
            f'{self.get_object().name} desativado com sucesso!'
        )
        return super().form_valid(form)
    

class DetailUserView(LoginRequiredMixin, DetailView):

    model = User
    template_name = 'accounts/detail.html'
    