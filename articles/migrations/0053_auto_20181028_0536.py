# Generated by Django 2.0.5 on 2018-10-28 05:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0052_auto_20181028_0526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='date_create',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 28, 5, 36, 15, 912626), verbose_name='Date Created'),
        ),
        migrations.AlterField(
            model_name='content',
            name='date_update',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 28, 5, 36, 15, 912727), verbose_name='Date Update'),
        ),
    ]
