# Generated by Django 2.0.5 on 2018-10-24 22:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0034_auto_20181024_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='date_create',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 24, 22, 57, 57, 505621), verbose_name='Date Created'),
        ),
        migrations.AlterField(
            model_name='content',
            name='date_update',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 24, 22, 57, 57, 505702), verbose_name='Date Update'),
        ),
    ]
