from django.db import models


class GuiaContents(models.Model):
    """
    GuiaContents model
    """
    title = models.CharField(max_length=200)
    priority = models.IntegerField(default=1)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "GuiaContents - {} - {}".format(self.parent.title, self.title)