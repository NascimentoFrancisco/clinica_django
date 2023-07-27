from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.db import IntegrityError
from django.views.generic import (
    CreateView, ListView, DetailView, DeleteView,
    UpdateView
)
from django.contrib.auth.mixins import LoginRequiredMixin

from clinic_app.models.patient_consultation import PatientConsultation
from clinic_app.models.accounts import User
from clinic_app.models.patient import Patient
from clinic_app.models.medical_schedule import MedicalSchedule
from clinic_app.views.accounts_views import TestMixinIsAdmin


class CreatePatientConsultationView(LoginRequiredMixin, CreateView):

    model = PatientConsultation
    template_name = 'patient_consultation/create.html'
    fields = []
    success_url = reverse_lazy('home')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        medical_schedule: MedicalSchedule = MedicalSchedule.objects.get(id=self.kwargs['pk'])
        try:  
            form.instance.patient = Patient.objects.get(user=self.request.user)
            form.instance.doctor_schedule = medical_schedule
            form.save()
            medical_schedule.status = False
            medical_schedule.save()
        except IntegrityError as e:
            if 'UNIQUE constraint failed' in e.args[0]:
                messages.warning(self.request, 'Não é possível você marcar essa consulta.')
                return HttpResponseRedirect(
                    reverse_lazy(
                        'create_patient_consultation', kwargs={'pk': medical_schedule.pk}
                    )
                )
        except Patient.DoesNotExist:
            messages.warning(self.request, 'Faça cadastro para poder reservar uma consulta')
            return HttpResponseRedirect(reverse_lazy('create_patient_user'))
        messages.success(self.request, 'Sua onsulta foi marcada com sucesso!')
        return HttpResponseRedirect(reverse_lazy('home'))


class ListPatientConsultationView(LoginRequiredMixin, ListView):

    model = PatientConsultation
    template_name = 'patient_consultation/list.html'
    paginate_by = 3
    
    def get_queryset(self) -> QuerySet[Any]:
        query_set = PatientConsultation.objects.filter(patient=self.request.user.patient)
        return query_set

class ListAllPatientConsultationView(LoginRequiredMixin, TestMixinIsAdmin, ListView):
    
    model = PatientConsultation
    template_name = 'patient_consultation/list.html'
    paginate_by = 3

class ListPatientConsultationActiveView(LoginRequiredMixin, ListView):

    model = PatientConsultation
    template_name = 'patient_consultation/list.html'
    paginate_by = 3
    
    def get_queryset(self) -> QuerySet[Any]:
        query_set = PatientConsultation.objects.filter(patient=self.request.user.patient, status=True)
        return query_set


class DetailPatientConsultationView(LoginRequiredMixin, DetailView):

    model = PatientConsultation
    template_name = 'patient_consultation/detail.html'


class DeletePatientConsultationView(LoginRequiredMixin, DeleteView):

    model = PatientConsultation
    template_name = 'patient_consultation/delete.html'
    success_url = reverse_lazy('list_patient_consultation')

    def form_valid(self, form) -> HttpResponse:
        medical_schedule: MedicalSchedule = MedicalSchedule.objects.get(
            patientconsultation = self.get_object()
        )
        self.get_object().delete()
        medical_schedule.status = True
        medical_schedule.save()
        messages.success(
            self.request, 'Consulta cancelada com sucesso!'
        )
        return HttpResponseRedirect(self.get_success_url())

class FinishPatientConsultationView(LoginRequiredMixin, TestMixinIsAdmin, UpdateView):

    model = PatientConsultation
    template_name = 'patient_consultation/finish.html'
    fields = []
    success_url = reverse_lazy('list_patient_consultation_all')
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.status = False
        form.save()
        return super().form_valid(form)

    def get_success_url(self) -> str:
        messages.success(
            self.request, 'Consulta finalizada!'
        )
        return super().get_success_url()
    