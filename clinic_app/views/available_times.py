from django.contrib import messages
from django.urls import reverse_lazy

from django.views.generic import (
    CreateView, ListView, DeleteView, UpdateView
)
from django.contrib.auth.mixins import LoginRequiredMixin

from clinic_app.models.available_times import AvailableTimes
from clinic_app.views.accounts_views import TestMixinIsAdmin
from clinic_app.forms.available_times_form import AvailableTimesCreationForm


class CreateAvailableTimesView(LoginRequiredMixin, TestMixinIsAdmin, CreateView):

    model = AvailableTimes
    template_name = 'available_times/create.html'
    form_class = AvailableTimesCreationForm
    success_url = reverse_lazy('list_available_times')

    def get_success_url(self) -> str:
        messages.success(
            self.request, 'Horário criado com suceso!'
        )
        return super().get_success_url()


class ListAvailableTimesView(LoginRequiredMixin, TestMixinIsAdmin, ListView):

    model = AvailableTimes
    template_name = 'available_times/list.html'
    paginate_by = 4


class UpdateAvailableTimesView(LoginRequiredMixin, TestMixinIsAdmin, UpdateView):

    model = AvailableTimes
    template_name = 'available_times/create.html'
    form_class = AvailableTimesCreationForm
    success_url = reverse_lazy('list_available_times')

    def get_success_url(self) -> str:
        messages.success(
            self.request, 'Horário alterado com suceso!'
        )
        return super().get_success_url()


class DeleteAvailableTimesView(LoginRequiredMixin, TestMixinIsAdmin, DeleteView):

    model = AvailableTimes
    template_name = 'available_times/delete.html'
    success_url = reverse_lazy('list_available_times')

    def get_success_url(self) -> str:
        messages.success(
            self.request, 'Horário excluído com suceso!'
        )
        return super().get_success_url()