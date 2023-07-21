from clinic_app.models import *

class AvailableTimes(models.Model):
    
    time_start = models.TimeField("Horaário de início")
    time_end = models.TimeField("Horaário de finalização")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f'{self.time_start} - {self.time_end}'