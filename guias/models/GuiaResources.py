from django.db import models


class GuiaResources(models.Model):
    """
    GuiaResources model
    """
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    author = models.CharField(max_length=200, null=True)
    editorial = models.CharField(max_length=200, null=True)
    href = models.CharField(max_length=200, null=True)
    type = models.CharField(max_length=200, default="a")
    year = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Resource - {} - {}".format(self.type, self.title)
