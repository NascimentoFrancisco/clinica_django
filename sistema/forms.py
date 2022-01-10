from django import forms
from sistema.models import Especialidade, Medico, Horarios, Agenda, Cliente
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from datetime import date
#import datetime

class EspecialidadeForm(forms.ModelForm):
    class Meta:
        model = Especialidade
        fields = '__all__'

class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ('nome','crm','email','telefone','especialidade')

        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'crm': forms.TextInput(attrs= {'class':'form-control'}),
            'email':forms.TextInput(attrs= {'class':'form-control','placeholder':'clinicadjango@gmail.com'}),
            'telefone':forms.TextInput(attrs= {'class':'form-control','placeholder':'99 99999-9999'}),
            'especialidade':forms.Select(attrs={'class':'form-control'}),
        }

class HorariosForm(forms.ModelForm):
    class Meta:
        model = Horarios
        fields = '__all__'

class AgendaForm(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = ('medico','data','horarios')

        widgets = {
            'medico':forms.Select(attrs={'class':'form-control'}),
            'data': forms.SelectDateWidget(),
            'horarios':forms.SelectMultiple(attrs={'class':'form-control'}),
        }
    
    def clean(self):
        super(AgendaForm, self).clean()

        data = self.cleaned_data.get('data')
        data_hj = date.today()

        if data < data_hj:
            self.errors['data'] = self.error_class(['Não é possível selecionar uma data já passada!'])

        medico = self.cleaned_data.get('medico')
        agenda_medico = Agenda.objects.filter(medico__id = medico.id)
        
        for agenda in agenda_medico:
            if data == agenda.data:
                self.errors['data'] = self.error_class(['Não é possível criar duas agendas na mesma data para um unico médico!'])           
                break          

        return self.cleaned_data

class ClienteForm(UserCreationForm):
    class Meta:
        model = Cliente
        fields = ('nome','cpf','email','sexo','telefone','username','password1', 'password2',)

        widgets = {
            'nome': forms.TextInput(attrs={ 'class': 'form-control', }),
            'cpf': forms.TextInput(attrs={ 'class': 'form-control', }),
            'email': forms.TextInput(attrs={ 'class': 'form-control', }),            
            'sexo': forms.Select(attrs={ 'class': 'form-control', }),
            'telefone': forms.TextInput(attrs={ 'class': 'form-control', }),                        
            'username': forms.TextInput(attrs={ 'class': 'form-control',}),
            'password1': forms.TextInput(attrs={ 'class': 'form-control',}),
            'password2': forms.TextInput(attrs={ 'class': 'form-control',}),                        
        }


