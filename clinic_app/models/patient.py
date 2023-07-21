from django.conf import settings
from clinic_app.models import *

class Patient(models.Model):


    patient_cpf = models.CharField(
        "CPF", max_length=11, unique=True, 
        error_messages={'unique':'Este CPF já está cadastrado no sistema.'},
        help_text='CPF do paciente sem pontos e traços'
    )
    phone = models.CharField(
        "Telefone", max_length=11,
        help_text="Telefone nesse formato 88900000000 sem espaços e traços, com o DD"
    )
    user: User = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        verbose_name='Usuário', 
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.user.name