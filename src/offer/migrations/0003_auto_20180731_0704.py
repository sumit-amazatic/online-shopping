# Generated by Django 2.0.7 on 2018-07-31 07:04

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0002_auto_20180730_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='code',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='days',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='offer',
            name='max_count',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
