from django import forms
from clinic_app.models import AvailableTimes



class AvailableTimesCreationForm(forms.ModelForm):

    class Meta:
        model = AvailableTimes
        fields = ['time_start', 'time_end']

        widgets = {
            'time_start': forms.TextInput(
                attrs={'type':'time'}
            ),
            'time_end': forms.TextInput(
                attrs={'type':'time'}
            ),
        }
    