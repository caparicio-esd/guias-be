from django.db import models


class GuiaCompetencies(models.Model):
    """
    GuiaCompetencies model
    """
    key = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=20)
    specialty = models.CharField(max_length=20, null=True)
    description = models.TextField()

    def __str__(self):
        return "GuiaCompetencies - {} - {}".format(self.key, self.title)

