# Generated by Django 2.1.4 on 2018-12-20 08:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_auto_20181220_0649'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventpage',
            name='age_policy',
            field=models.PositiveIntegerField(default=3, validators=[django.core.validators.MaxValueValidator(18), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='eventpage',
            name='event_time',
            field=models.DateField(null=True),
        ),
    ]
