from django.db import models


class GuiaResults(models.Model):
    """
    GuiaResults model
    """
    title = models.CharField(max_length=200)
    description = models.TextField()
    priority = models.IntegerField(default=1)

    def __str__(self):
        return "Results - {}".format(self.title)