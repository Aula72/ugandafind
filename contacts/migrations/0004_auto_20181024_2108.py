# Generated by Django 2.0.5 on 2018-10-24 21:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_auto_20181024_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2018, 10, 24, 21, 8, 10, 503379, tzinfo=utc)),
        ),
    ]