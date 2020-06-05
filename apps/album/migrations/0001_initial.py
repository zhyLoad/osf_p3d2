# Generated by Django 2.1.3 on 2018-11-13 09:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tag', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('create_ts', models.DateTimeField(default=datetime.datetime(2018, 11, 13, 17, 41, 27, 395193))),
                ('album_title', models.CharField(default='New Album', max_length=100)),
                ('album_desc', models.CharField(blank=True, max_length=200)),
                ('last_add_ts', models.DateTimeField(auto_now=True)),
                ('photos_count', models.IntegerField(default=0)),
                ('status', models.IntegerField(default=0)),
                ('cover', models.URLField(default='http://7xjfbe.com1.z0.glb.clouddn.com/23.jpg')),
                ('like_count', models.IntegerField(default=0)),
                ('share_count', models.IntegerField(default=0)),
                ('comment_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('key', models.CharField(blank=True, max_length=100)),
                ('album_id', models.IntegerField(blank=True, default=0)),
                ('ts', models.DateTimeField(default=datetime.datetime(2018, 11, 13, 17, 41, 27, 394193))),
                ('desc', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='photos',
            field=models.ManyToManyField(to='album.Photo'),
        ),
        migrations.AddField(
            model_name='album',
            name='tags',
            field=models.ManyToManyField(to='tag.Tag'),
        ),
    ]