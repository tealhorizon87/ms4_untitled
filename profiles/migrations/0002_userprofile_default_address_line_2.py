# Generated by Django 3.2.7 on 2022-01-08 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='default_address_line_2',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
