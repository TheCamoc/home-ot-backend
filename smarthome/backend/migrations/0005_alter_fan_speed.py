# Generated by Django 4.0.10 on 2023-05-25 19:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_fan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fan',
            name='speed',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
