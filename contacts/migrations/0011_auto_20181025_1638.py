# Generated by Django 2.0.5 on 2018-10-25 16:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0010_auto_20181025_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2018, 10, 25, 16, 38, 17, 881042, tzinfo=utc)),
        ),
    ]
