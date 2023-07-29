from typing import Any
from django.db.models import Model
from django.contrib import messages
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.db import transaction
from django.views.generic import (
    CreateView, DetailView, UpdateView, ListView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from clinic_app.models.patient import Patient
from clinic_app.models.accounts import User
from clinic_app.forms.user_form import CreationUserForm, ChangeUserForm
from clinic_app.forms.patient_form import (
    PatientCreationForm, PatientUpdateForm
)
from clinic_app.views.accounts_views import TestMixinIsAdmin


class CreatePatientUserView(CreateView):

    model = Patient
    template_name = "patient/create.html"
    form_class = PatientCreationForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['user_form'] = CreationUserForm(self.request.POST)
        else:
            context['user_form'] = CreationUserForm()
        return context
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        context = self.get_context_data()
        user_form: BaseModelForm = context['user_form']

        with transaction.atomic():
            user: User = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password1'])
            user.save()

            patient: Patient = form.save(commit=False)
            patient.user = user
            patient.save()

        return super().form_valid(form)


class ListPatientView(LoginRequiredMixin, TestMixinIsAdmin, ListView):
    
    model = Patient
    template_name = 'patient/list.html'
    paginate_by = 4

    def get_queryset(self) -> QuerySet[Any]:
        query_set = super().get_queryset()
        patient_cpf = self.request.GET.get('cpf', None)

        if patient_cpf:
            query_set = Patient.objects.filter(patient_cpf=patient_cpf)
        return query_set


class DetailPatientView(LoginRequiredMixin, DetailView):

    model = Patient
    template_name = 'patient/detail.html'
    
    def get_object(self, queryset=None) -> Model:
        object = Patient.objects.get(user=self.request.user)
        return object


class UpdatePatientUserView(LoginRequiredMixin, UpdateView):

    model = Patient
    template_name = "patient/create.html"
    form_class = PatientUpdateForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['user_form'] = ChangeUserForm(self.request.POST, instance=self.get_object().user)
        else:
            context['user_form'] = ChangeUserForm(instance=self.get_object().user)
        return context
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        context = self.get_context_data()
        user_form: BaseModelForm = context['user_form']
        
        with transaction.atomic():
            
            user_form = ChangeUserForm(self.request.POST, instance=self.get_object().user)
            
            if user_form.is_valid():
                user_form.save()
            else:
                context['user_form'] = user_form
                return self.render_to_response(context)
            
            form.save()

        return super().form_valid(form)
    
    def get_success_url(self) -> str:
        messages.success(
            self.request, 'Dados alterados com sucesso!'
        )
        return super().get_success_url()
    