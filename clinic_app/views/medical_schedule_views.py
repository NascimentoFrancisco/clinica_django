from typing import Any
from django.contrib import messages
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, UpdateView, DeleteView, ListView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from clinic_app.views.accounts_views import TestMixinIsAdmin

from clinic_app.models.medical_schedule import MedicalSchedule
from clinic_app.forms.create_medical_schedule_form import MedicalScheduleCreationForm


class CreateMedicalScheduleView(LoginRequiredMixin, TestMixinIsAdmin, CreateView):

    model = MedicalSchedule
    template_name = 'medical_schedule/create.html'
    success_url = reverse_lazy('list_medical_schedule')
    form_class = MedicalScheduleCreationForm

    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        try:
            if form.errors.get_json_data(escape_html=False)['__all__'][0]['code'] == 'unique_together':
                form.errors.clear()
                form.add_error("date_schedule","Agenda para esse(a) médico(a) nessa data já existe")
                form.add_error("available_times","Agenda para esse(a) médico(a) nesse horário já existe")
        except KeyError:
            pass
        return super().form_invalid(form)
    
    def get_success_url(self) -> str:
        messages.success(
            self.request, 
            f'Agenda para o(a) médico(a) "{self.get_form().data["doctor"]}" criada com sucesso!'
        )
        return super().get_success_url()


class ListMedicalScheduleView(ListView):

    model = MedicalSchedule
    template_name = 'medical_schedule/list.html'
    paginate_by = 3


class DetailMedicalScheduleView(DeleteView):

    model = MedicalSchedule
    template_name = 'medical_schedule/detail.html'


class UpdateMedicalScheduleView(LoginRequiredMixin, TestMixinIsAdmin, UpdateView):

    model = MedicalSchedule
    template_name = 'medical_schedule/create.html'
    success_url = reverse_lazy('list_medical_schedule')
    form_class = MedicalScheduleCreationForm

    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        try:
            if form.errors.get_json_data(escape_html=False)['__all__'][0]['code'] == 'unique_together':
                form.errors.clear()
                form.add_error("date_schedule","Agenda para esse(a) médico(a) nessa data já existe")
                form.add_error("available_times","Agenda para esse(a) médico(a) nesse horário já existe")
        except KeyError:
            pass
        return super().form_invalid(form)
    
    def get_success_url(self) -> str:
        messages.success(
            self.request, 
            f'Agenda para o(a) médico(a) "{self.get_object().doctor.name}" criada com sucesso!'
        )
        return super().get_success_url()


class DeleteMedicalScheduleView(LoginRequiredMixin, TestMixinIsAdmin, DeleteView):

    model = MedicalSchedule
    template_name = 'medical_schedule/delete.html'
    success_url = reverse_lazy('list_medical_schedule')

    def get_success_url(self) -> str:
        messages.success(
            self.request, 
            f'Agenda "{self.get_object()}" excluída com sucesso!'
        )
        return super().get_success_url()


class ListMedicalScheduleForPatientView(ListView):

    model = MedicalSchedule
    template_name = 'medical_schedule/list.html'
    paginate_by = 3

    def get_queryset(self) -> QuerySet[Any]:
        queryset = MedicalSchedule.objects.filter(doctor__id=self.kwargs['pk'], status=True)
        return queryset