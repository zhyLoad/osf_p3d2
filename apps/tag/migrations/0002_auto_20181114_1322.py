# Generated by Django 2.1.3 on 2018-11-14 05:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='add_ts',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 14, 13, 22, 38, 570122)),
        ),
    ]
