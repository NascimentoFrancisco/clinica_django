from django.contrib import messages
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, UpdateView, DeleteView, ListView
)
from django.contrib.auth.mixins import LoginRequiredMixin

from clinic_app.views.accounts_views import TestMixinIsAdmin
from clinic_app.models.specialty import Specialty
from clinic_app.forms.specialty_form import SpecialtyForm

class CreateSpecialtyView(LoginRequiredMixin, TestMixinIsAdmin, CreateView):

    model = Specialty
    template_name = "specialty/create.html"
    form_class = SpecialtyForm
    success_url = reverse_lazy('list_specialty')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        messages.success(
            self.request, f'Especialidade "{form.data["name"]}" criada com sucesso!'
        )
        return super().form_valid(form)

class ListSpecialtyView(LoginRequiredMixin, TestMixinIsAdmin, ListView):

    model = Specialty
    template_name = "specialty/list.html"
    paginate_by = 3


class UpdateSpecialtyView(LoginRequiredMixin, TestMixinIsAdmin, UpdateView):

    model = Specialty
    template_name = "specialty/create.html"
    form_class = SpecialtyForm
    success_url = '/specialty/list/'

    def get_success_url(self) -> str:
        messages.success(
            self.request, f'Especialidade "{self.get_object().name}" alterada com sucesso!'
        )
        return super().get_success_url()


class DeleteSpecialtyView(LoginRequiredMixin, TestMixinIsAdmin, DeleteView):

    model = Specialty
    template_name = "specialty/delete.html"
    success_url = '/specialty/list/'

    def get_success_url(self) -> str:
        messages.success(
            self.request, f'Especialidade "{self.get_object().name}" apagada com sucesso!'
        )
        return super().get_success_url()