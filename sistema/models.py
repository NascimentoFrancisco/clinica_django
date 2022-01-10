from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Especialidade(models.Model):
    nome = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.nome

class Medico(models.Model):
    nome = models.CharField(max_length=200, blank=False, null=False)
    crm = models.CharField(max_length=30, blank=False, null=False)
    email = models.EmailField()
    telefone = models.CharField(max_length=17)
    especialidade = models.ForeignKey(Especialidade, on_delete= models.CASCADE, verbose_name='Especialidade',blank=False)

    def __str__(self):
        return self.nome

class Horarios(models.Model):
    horas = models.CharField(max_length=5, blank=False, null=False)

    def __str__(self):
        return self.horas

class Agenda(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, verbose_name='Médico Especialista',blank=False)
    data = models.DateField()
    horarios = models.ManyToManyField(Horarios, blank= False)

    def __str__(self):
        return str(self.medico.nome)

class Cliente(User):
    SEXO_CHOISES = (
        ('M','Masculino'),
        ('F','Feminino')
    )
    nome = models.CharField(max_length=200, blank=False, null=False)
    cpf = models.CharField(max_length=14, blank=False, null=False)
    sexo = models.CharField(max_length=1,choices=SEXO_CHOISES,blank=False, null=False)
    telefone = models.CharField(max_length=16)
    consulta = models.ManyToManyField(Agenda, blank=True)
    
    def __str__(self):
        return self.nome
