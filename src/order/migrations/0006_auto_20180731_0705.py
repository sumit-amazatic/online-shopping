# Generated by Django 2.0.7 on 2018-07-31 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_auto_20180730_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentmethod',
            name='slug',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
