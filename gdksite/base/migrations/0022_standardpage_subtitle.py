# Generated by Django 2.1.4 on 2019-01-01 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0021_collectivepage_subtitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='standardpage',
            name='subtitle',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
