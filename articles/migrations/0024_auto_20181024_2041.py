# Generated by Django 2.0.5 on 2018-10-24 20:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0023_auto_20181024_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='date_create',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 24, 20, 41, 37, 439480), verbose_name='Date Created'),
        ),
        migrations.AlterField(
            model_name='content',
            name='date_update',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 24, 20, 41, 37, 439552), verbose_name='Date Update'),
        ),
    ]
