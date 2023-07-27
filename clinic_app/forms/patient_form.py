from django import forms
from clinic_app.models import Patient
from clinic_app.forms.user_form import CreationUserForm, ChangeUserForm


class PatientCreationForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields = ['patient_cpf', 'phone']
    
    user_form = CreationUserForm()


class PatientUpdateForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields = ['patient_cpf', 'phone']
    
    user_form = ChangeUserForm()