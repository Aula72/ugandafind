# Generated by Django 2.0 on 2018-11-02 22:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0025_auto_20181028_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2018, 11, 2, 22, 9, 48, 163564, tzinfo=utc)),
        ),
    ]
