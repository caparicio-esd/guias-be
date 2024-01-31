from datetime import datetime

from django.db import models
from django.utils.timezone import now


class GuiaSpecialty(models.Model):
    """
    GuiaSpecialty model
    """
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return "Specialty - {}".format(self.title)
