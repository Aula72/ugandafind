# Generated by Django 2.0.5 on 2018-10-24 20:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0017_auto_20181024_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='date_create',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 24, 20, 29, 52, 150340), verbose_name='Date Created'),
        ),
        migrations.AlterField(
            model_name='content',
            name='date_update',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 24, 20, 29, 52, 150423), verbose_name='Date Update'),
        ),
    ]