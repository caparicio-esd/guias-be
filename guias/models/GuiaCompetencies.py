from django.db import models


class GuiaCompetencies(models.Model):
    """
    GuiaCompetencies model
    """
    key = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=20)
    specialty = models.CharField(max_length=20)
    description = models.TextField(default="", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "GuiaCompetencies - {} - {}".format(self.key, self.title)

