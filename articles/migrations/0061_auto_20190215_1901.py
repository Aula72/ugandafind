# Generated by Django 2.0.2 on 2019-02-15 16:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0060_auto_20190215_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='date_create',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 19, 1, 18, 187115), verbose_name='Date Created'),
        ),
        migrations.AlterField(
            model_name='content',
            name='date_update',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 19, 1, 18, 187115), verbose_name='Date Update'),
        ),
    ]
