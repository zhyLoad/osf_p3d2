# Generated by Django 2.1.3 on 2018-11-14 07:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('like', '0002_auto_20181114_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='ts',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 14, 15, 21, 19, 138122)),
        ),
    ]
