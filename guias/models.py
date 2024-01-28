from django.db import models


# Create your models here.
class Guia(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class GuiaField(models.Model):
    field_key = models.CharField(max_length=200)
    field_value = models.CharField(max_length=200)
    field_type = models.CharField(max_length=200)
    guia = models.ForeignKey(Guia, on_delete=models.CASCADE)

    def __str__(self):
        return "{}-{}-{}".format(
            self.field_key,
            self.field_value,
            self.field_type
        )
