from django.contrib.auth.models import User
from django.db import models

from guias.models.GuiaCompetencies import GuiaCompetencies
from guias.models.GuiaSpecialty import GuiaSpecialty
from guias.models.GuiaResults import GuiaResults
from guias.models.GuiaContents import GuiaContents
from guias.models.GuiaResources import GuiaResources
from guias.models.GuiaChronogram import GuiaChronogram


class Guia(models.Model):
    """
    Guia model
    """
    # Generic data
    title = models.CharField(max_length=500, null=True)
    description = models.TextField(null=True)
    course_code = models.CharField(max_length=300, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Identifiers
    identifier_type = models.CharField(max_length=200, null=True)
    identifier_character = models.CharField(max_length=200, null=True)
    identifier_specialty = models.ForeignKey(GuiaSpecialty, on_delete=models.CASCADE, null=True)
    identifier_subject = models.CharField(max_length=200, null=True)
    identifier_course = models.CharField(max_length=200, null=True)
    identifier_semester = models.CharField(max_length=2, null=True)
    identifier_credits = models.IntegerField(default=0)
    identifier_hours_total = models.IntegerField(default=0)
    identifier_hours_presence = models.IntegerField(default=0, null=True)
    identifier_department = models.CharField(max_length=200, null=True)
    identifier_prelation = models.TextField(blank=True, null=True)
    identifier_language = models.CharField(max_length=200, null=True)

    # User relation
    coordinator = models.ForeignKey(User, on_delete=models.PROTECT, null=True, related_name='coordinator')
    teachers = models.ManyToManyField(User)

    # Many-to-many relations
    competencies = models.ManyToManyField(GuiaCompetencies)
    results = models.ManyToManyField(GuiaResults)
    contents = models.ManyToManyField(GuiaContents)

    # Hours
    hours_activities = models.IntegerField(default=0)
    hours_probes = models.IntegerField(default=0)
    hours_selfwork = models.IntegerField(default=0)
    hours_preparatioin = models.IntegerField(default=0)

    # Methodology
    methodology_theory = models.TextField(null=True)
    methodology_practical = models.TextField(null=True)
    methodology_others = models.TextField(null=True)

    # Evaluation
    eval_instruments_theory = models.TextField(null=True)
    eval_instruments_practical = models.TextField(null=True)
    eval_instruments_others = models.TextField(null=True)
    eval_criteria_theory = models.TextField(null=True)
    eval_criteria_practical = models.TextField(null=True)
    eval_criteria_others = models.TextField(null=True, default="No criteria")

    # Calification
    calification_continual_evaluation_theory = models.IntegerField(default=0)
    calification_continual_evaluation_practical = models.IntegerField(default=0)
    calification_continual_evaluation_attitude = models.IntegerField(default=0)
    calification_ordinary = models.IntegerField(default=0)
    calification_extraordinary = models.IntegerField(default=0)
    calification_disabled_theory = models.IntegerField(default=0)
    calification_disabled_practical = models.IntegerField(default=0)
    calification_disabled_attitude = models.IntegerField(default=0)

    # Chronogram
    chronogram = models.ForeignKey(GuiaChronogram, on_delete=models.CASCADE, null=True)

    # Resources
    resources = models.ManyToManyField(GuiaResources, default=0)

    def __str__(self):
        return self.title
