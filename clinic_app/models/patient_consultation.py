from clinic_app.models import *

class PatientConsultation(models.Model):
    

    doctor_schedule = models.OneToOneField(MedicalSchedule, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    status = models.BooleanField('Status', default=True, help_text='Situação da consulta')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('doctor_schedule', 'patient')
        
    def __str__(self) -> str:
        return f'{self.doctor_schedule} - {self.patient}'
