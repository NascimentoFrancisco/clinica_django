from clinic_app.models import *

class Specialty(models.Model):

    name = models.CharField("Especialidade", max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name