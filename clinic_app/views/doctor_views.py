from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, UpdateView, DeleteView, ListView, DetailView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from clinic_app.views.accounts_views import TestMixinIsAdmin

from clinic_app.models.doctor import Doctor


class CreateDoctorView(LoginRequiredMixin, TestMixinIsAdmin, CreateView):

    model = Doctor
    template_name = 'doctor/create.html'
    fields = ['name', 'medical_cpf', 'specialty', 'medical_crm', 'phone', 'email']
    success_url = reverse_lazy('list_doctor')

    def get_success_url(self) -> str:
        
        messages.success(
            self.request, f'Médico(a) "{self.get_form().data["name"]}" criado(a) com sucesso!'
        )
        return super().get_success_url()
    

class ListdoctorView(ListView):

    model = Doctor
    template_name = 'doctor/list.html'
    paginate_by = 3


class DetailDoctorView(DetailView):

    model = Doctor
    template_name = 'doctor/detail.html'

class UpdateDoctorView(LoginRequiredMixin, TestMixinIsAdmin, UpdateView):

    model = Doctor
    template_name = 'doctor/create.html'
    fields = ['name', 'medical_cpf', 'specialty', 'medical_crm', 'phone', 'email']
    success_url = reverse_lazy('list_doctor')

    def get_success_url(self) -> str:
        messages.success(
            self.request, f'Médico(a) "{self.get_object().name}" alterado(a) com sucesso!'
        )
        return super().get_success_url()

class DeleteDoctorView(LoginRequiredMixin, TestMixinIsAdmin, DeleteView):

    model = Doctor
    template_name = 'doctor/delete.html'
    success_url = reverse_lazy('list_doctor')

    def get_success_url(self) -> str:
        messages.success(
            self.request, f'Médico(a) "{self.get_object().name}" excluido(a) com sucesso!'
        )
        return super().get_success_url()