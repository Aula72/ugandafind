# Generated by Django 2.0.5 on 2018-10-28 05:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0050_auto_20181028_0018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='date_create',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 28, 5, 25, 20, 651809), verbose_name='Date Created'),
        ),
        migrations.AlterField(
            model_name='content',
            name='date_update',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 28, 5, 25, 20, 651877), verbose_name='Date Update'),
        ),
    ]
