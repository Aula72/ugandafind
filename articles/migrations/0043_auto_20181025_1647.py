# Generated by Django 2.0.5 on 2018-10-25 16:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0042_auto_20181025_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='date_create',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 25, 16, 47, 3, 387384), verbose_name='Date Created'),
        ),
        migrations.AlterField(
            model_name='content',
            name='date_update',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 25, 16, 47, 3, 387453), verbose_name='Date Update'),
        ),
    ]
