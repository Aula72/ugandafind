# Generated by Django 2.0.5 on 2018-10-24 21:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0029_auto_20181024_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='date_create',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 24, 21, 1, 20, 458876), verbose_name='Date Created'),
        ),
        migrations.AlterField(
            model_name='content',
            name='date_update',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 24, 21, 1, 20, 458952), verbose_name='Date Update'),
        ),
    ]
