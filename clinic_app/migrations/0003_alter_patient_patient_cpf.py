# Generated by Django 4.2.3 on 2023-08-01 15:54

import clinic_app.validators.validate_cpf
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic_app', '0002_patientconsultation_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='patient_cpf',
            field=models.CharField(error_messages={'unique': 'Este CPF já está cadastrado no sistema.'}, help_text='CPF do paciente sem pontos e traços', max_length=11, unique=True, validators=[clinic_app.validators.validate_cpf.cpf_validate], verbose_name='CPF'),
        ),
    ]
