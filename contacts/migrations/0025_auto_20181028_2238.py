# Generated by Django 2.0.5 on 2018-10-28 22:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0024_auto_20181028_0536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2018, 10, 28, 22, 38, 42, 463556, tzinfo=utc)),
        ),
    ]
