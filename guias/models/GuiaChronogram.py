from django.db import models


class GuiaChronogram(models.Model):
    """
    GuiaChronogram model
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "GuiaChronogram - {}".format(self.id)


class GuiaChronogramBlocks(models.Model):
    """
    GuiaChronogramBlocks model
    """
    time_entity = models.IntegerField()
    block = models.IntegerField()
    theme = models.IntegerField()
    exercise = models.CharField(max_length=200, null=True)
    exercise_content = models.CharField(max_length=1000, null=True)
    competencies = models.CharField(max_length=1000, null=True)
    exam = models.CharField(max_length=20, default=None, null=True)
    special_activity = models.CharField(max_length=200, default=None, null=True)
    chronogram = models.ForeignKey(GuiaChronogram, on_delete=models.CASCADE, related_name='blocks')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "GuiaChronogramBlocks - {} - {}".format(self.chronogram.id, self.time_entity)

