# Generated by Django 2.0.5 on 2018-10-24 23:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0005_auto_20181024_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2018, 10, 24, 23, 2, 44, 628508, tzinfo=utc)),
        ),
    ]
