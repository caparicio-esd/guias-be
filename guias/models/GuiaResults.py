from django.db import models


class GuiaResults(models.Model):
    """
    GuiaResults model
    """
    title = models.CharField(max_length=200)
    description = models.TextField()
    priority = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Results - {}".format(self.title)