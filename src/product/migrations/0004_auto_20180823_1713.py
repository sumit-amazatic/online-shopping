# Generated by Django 2.0.7 on 2018-08-23 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20180816_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='seller',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='seller.Seller'),
        ),
    ]
