# Generated by Django 2.0.7 on 2018-07-21 23:26

import datetime
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('78d0250b-96a5-4dbf-ac24-e7aaf8661c0f'), primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=1024)),
                ('year', models.IntegerField()),
                ('ids', jsonfield.fields.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WatchlistMovie',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('4700ae15-8f6b-41b7-9cb9-5cd4e866ccef'), primary_key=True, serialize=False)),
                ('rank', models.IntegerField()),
                ('type', models.CharField(default='movie', max_length=64)),
                ('listed_at', models.DateTimeField(default=datetime.datetime(2018, 7, 21, 23, 26, 33, 146587))),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recommendation.Movie', verbose_name='Movie watched')),
            ],
        ),
    ]
