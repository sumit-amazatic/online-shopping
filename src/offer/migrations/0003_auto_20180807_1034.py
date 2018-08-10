# Generated by Django 2.0.7 on 2018-08-07 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0002_auto_20180803_1548'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='offer',
            name='offer_index',
        ),
        migrations.RemoveIndex(
            model_name='offerlineitem',
            name='offer_lineitem_index',
        ),
        migrations.RemoveIndex(
            model_name='orderoffer',
            name='order_offer_index',
        ),
        migrations.RemoveIndex(
            model_name='productoffer',
            name='product_offer_index',
        ),
        migrations.RemoveIndex(
            model_name='useroffer',
            name='user_offer_index',
        ),
        migrations.RenameField(
            model_name='offerlineitem',
            old_name='lineitem_id',
            new_name='lineitem',
        ),
        migrations.RenameField(
            model_name='offerlineitem',
            old_name='offers_id',
            new_name='offer',
        ),
        migrations.RenameField(
            model_name='orderoffer',
            old_name='offers_id',
            new_name='offer',
        ),
        migrations.RenameField(
            model_name='orderoffer',
            old_name='order_id',
            new_name='order',
        ),
        migrations.RenameField(
            model_name='productoffer',
            old_name='offers_id',
            new_name='offers',
        ),
        migrations.RenameField(
            model_name='productoffer',
            old_name='product_id',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='useroffer',
            old_name='offers_id',
            new_name='offer',
        ),
        migrations.RenameField(
            model_name='useroffer',
            old_name='order_id',
            new_name='order',
        ),
        migrations.AlterField(
            model_name='offer',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='offerlineitem',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='offerlineitem',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='orderoffer',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='orderoffer',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='productoffer',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='productoffer',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='useroffer',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='useroffer',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, db_index=True),
        ),
        migrations.AddIndex(
            model_name='offer',
            index=models.Index(fields=['valid_from', 'valid_upto', 'name'], name='offer_index'),
        ),
    ]
