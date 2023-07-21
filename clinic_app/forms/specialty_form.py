from django.forms import ModelForm
from clinic_app.models.specialty import Specialty

class SpecialtyForm(ModelForm):

    class Meta:
        model = Specialty
        fields = ['name']

