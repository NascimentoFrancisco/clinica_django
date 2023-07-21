from django.core.exceptions import ValidationError
from django.utils import timezone
from clinic_app.models import *


def validate_future_date(value: models.DateField) -> None:

    if value < timezone.now().date():
        raise ValidationError("A data não pode ser no passado.")

class MedicalSchedule(models.Model):

    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date_schedule = models.DateField(
        "Data", help_text="Data para essa agenda",
        validators=[validate_future_date]
    )
    available_times = models.ForeignKey(
        AvailableTimes, on_delete=models.CASCADE,verbose_name="Horário"
    )
    status = models.BooleanField(
        "Status", default=True, help_text="Se a agenda está disponível para pacientes"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('available_times', 'date_schedule')

    def __str__(self) -> str:
        return f'{self.doctor} - {self.date_schedule.strftime("%b %d %Y")}'