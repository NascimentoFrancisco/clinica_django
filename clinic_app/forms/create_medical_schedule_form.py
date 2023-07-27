from django import forms
from clinic_app.models import MedicalSchedule


class MedicalScheduleCreationForm(forms.ModelForm):

    class Meta:
        model = MedicalSchedule
        fields = ['doctor', 'date_schedule', 'available_times', 'status']

        widgets = {
            'date_schedule':forms.TextInput(
                attrs={'type':'date'}
            ),
        }
    
    