# Generated by Django 2.0.5 on 2018-10-24 21:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0030_auto_20181024_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='date_create',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 24, 21, 2, 26, 861105), verbose_name='Date Created'),
        ),
        migrations.AlterField(
            model_name='content',
            name='date_update',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 24, 21, 2, 26, 861178), verbose_name='Date Update'),
        ),
    ]