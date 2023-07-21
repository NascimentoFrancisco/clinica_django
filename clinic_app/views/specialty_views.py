from django.urls import reverse_lazy
from django.views.generic import CreateView
from .specialty_views import *
from clinic_app.models.specialty import Specialty
from clinic_app.forms.specialty_form import SpecialtyForm

class CreateSpecialtyView(CreateView):

    model = Specialty
    template_name = "specialty/create.html"
    form_class = SpecialtyForm
    success_url = reverse_lazy('home')
    
