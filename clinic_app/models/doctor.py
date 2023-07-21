from clinic_app.models import *

class Doctor(models.Model):
    name = models.CharField("Nome", max_length=255)
    medical_cpf = models.CharField(
        "CPF", max_length=11, unique=True, 
        error_messages={'unique':'Este CPF já está cadastrado no sistema.'},
        help_text='CPF do médico sem pontos e traços'
    )
    specialty = models.ForeignKey(
        Specialty, on_delete=models.CASCADE,
        verbose_name='Especialidade'
    )
    medical_crm = models.CharField(
        "CRM", max_length=6, unique=True, 
        error_messages={'unique':'Este CRM já está cadastrado no sistema.'},
        help_text='CRM do médico sem pontos e traços'
    )
    phone = models.CharField(
        "Telefone", max_length=11,
        help_text="Telefone nesse formato 88900000000 sem espaços e traços, com o DD"
    )
    email = models.EmailField(
        'E-mail', unique=True,
        error_messages = {'unique' : "E-mail já cadastrado!"},
        help_text = 'Para envio de notificações se caso necessário.'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name