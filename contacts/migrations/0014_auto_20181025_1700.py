# Generated by Django 2.0.5 on 2018-10-25 17:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0013_auto_20181025_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2018, 10, 25, 17, 0, 10, 24898, tzinfo=utc)),
        ),
    ]
