# Generated by Django 5.0.1 on 2024-02-06 20:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GuiaChronogram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='GuiaCompetencies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=20)),
                ('specialty', models.CharField(max_length=20, null=True)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='GuiaResources',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(null=True)),
                ('author', models.CharField(max_length=200, null=True)),
                ('editorial', models.CharField(max_length=200, null=True)),
                ('href', models.CharField(max_length=200, null=True)),
                ('type', models.CharField(default='a', max_length=200)),
                ('year', models.IntegerField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='GuiaResults',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('priority', models.IntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='GuiaSpecialty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='GuiaChronogramBlocks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_entity', models.IntegerField()),
                ('block', models.IntegerField()),
                ('theme', models.IntegerField()),
                ('exercise', models.CharField(max_length=200, null=True)),
                ('exercise_content', models.CharField(max_length=1000, null=True)),
                ('competencies', models.CharField(max_length=1000, null=True)),
                ('exam', models.CharField(default=None, max_length=20, null=True)),
                ('special_activity', models.CharField(default=None, max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('chronogram', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blocks', to='guias.guiachronogram')),
            ],
        ),
        migrations.CreateModel(
            name='GuiaContents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('priority', models.IntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='guias.guiacontents')),
            ],
        ),
        migrations.CreateModel(
            name='Guia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField(null=True)),
                ('course_code', models.CharField(max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('published_at', models.DateTimeField(null=True)),
                ('year_code', models.IntegerField()),
                ('status', models.CharField(default='draft', max_length=200)),
                ('identifier_type', models.CharField(max_length=200, null=True)),
                ('identifier_character', models.CharField(max_length=200, null=True)),
                ('identifier_subject', models.CharField(max_length=200, null=True)),
                ('identifier_course', models.CharField(max_length=200, null=True)),
                ('identifier_semester', models.CharField(max_length=2, null=True)),
                ('identifier_credits', models.IntegerField(default=0)),
                ('identifier_hours_total', models.IntegerField(default=0)),
                ('identifier_hours_presence', models.IntegerField(default=0, null=True)),
                ('identifier_department', models.CharField(max_length=200, null=True)),
                ('identifier_prelation', models.TextField(blank=True, null=True)),
                ('identifier_language', models.CharField(max_length=200, null=True)),
                ('hours_activities', models.IntegerField(default=0)),
                ('hours_probes', models.IntegerField(default=0)),
                ('hours_selfwork', models.IntegerField(default=0)),
                ('hours_preparatioin', models.IntegerField(default=0)),
                ('methodology_theory', models.TextField(null=True)),
                ('methodology_practical', models.TextField(null=True)),
                ('methodology_others', models.TextField(null=True)),
                ('eval_instruments_theory', models.TextField(null=True)),
                ('eval_instruments_practical', models.TextField(null=True)),
                ('eval_instruments_others', models.TextField(null=True)),
                ('eval_criteria_theory', models.TextField(null=True)),
                ('eval_criteria_practical', models.TextField(null=True)),
                ('eval_criteria_others', models.TextField(default='No criteria', null=True)),
                ('calification_continual_evaluation_theory', models.IntegerField(default=0)),
                ('calification_continual_evaluation_practical', models.IntegerField(default=0)),
                ('calification_continual_evaluation_attitude', models.IntegerField(default=0)),
                ('calification_ordinary', models.IntegerField(default=0)),
                ('calification_extraordinary', models.IntegerField(default=0)),
                ('calification_disabled_theory', models.IntegerField(default=0)),
                ('calification_disabled_practical', models.IntegerField(default=0)),
                ('calification_disabled_attitude', models.IntegerField(default=0)),
                ('coordinator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='coordinator', to=settings.AUTH_USER_MODEL)),
                ('teachers', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
                ('chronogram', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='guias.guiachronogram')),
                ('competencies', models.ManyToManyField(blank=True, to='guias.guiacompetencies')),
                ('contents', models.ManyToManyField(blank=True, to='guias.guiacontents')),
                ('resources', models.ManyToManyField(blank=True, to='guias.guiaresources')),
                ('results', models.ManyToManyField(blank=True, to='guias.guiaresults')),
                ('identifier_specialty', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='guias.guiaspecialty')),
            ],
        ),
    ]
