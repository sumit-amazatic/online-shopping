# Generated by Django 2.0.7 on 2018-07-27 04:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20180726_0728'),
        ('product', '0002_auto_20180727_0442'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
            options={
                'db_table': 'wishlist',
            },
        ),
        migrations.AddIndex(
            model_name='wishlist',
            index=models.Index(fields=['created_at', 'updated_at'], name='wishlist_index'),
        ),
    ]
