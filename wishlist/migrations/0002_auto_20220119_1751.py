# Generated by Django 3.2.7 on 2022-01-19 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='wishlist_total',
        ),
        migrations.RemoveField(
            model_name='wishlistitem',
            name='product_size',
        ),
        migrations.RemoveField(
            model_name='wishlistitem',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='wishlistitem',
            name='wishlistitem_total',
        ),
    ]
