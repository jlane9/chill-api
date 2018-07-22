# Generated by Django 2.0.7 on 2018-07-22 05:15

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0005_auto_20180722_0408'),
    ]

    operations = [
        migrations.CreateModel(
            name='TraktSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_slug', models.CharField(max_length=1024)),
                ('token', models.CharField(max_length=128)),
            ],
        ),
        migrations.AlterField(
            model_name='episode',
            name='id',
            field=models.UUIDField(default=uuid.UUID('224070d8-ec58-492e-88cd-fae094e60ac9'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='historylistmovie',
            name='action',
            field=models.CharField(default='watch', max_length=64),
        ),
        migrations.AlterField(
            model_name='historylistmovie',
            name='id',
            field=models.UUIDField(default=uuid.UUID('ee45fea8-7d09-4f93-8036-5a20f785bd9d'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='historylistmovie',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recommendation.Movie', verbose_name='Movie watched'),
        ),
        migrations.AlterField(
            model_name='historylistmovie',
            name='type',
            field=models.CharField(default='movie', max_length=64),
        ),
        migrations.AlterField(
            model_name='historylistshow',
            name='action',
            field=models.CharField(default='watch', max_length=64),
        ),
        migrations.AlterField(
            model_name='historylistshow',
            name='episode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recommendation.Episode', verbose_name='Episode watched'),
        ),
        migrations.AlterField(
            model_name='historylistshow',
            name='id',
            field=models.UUIDField(default=uuid.UUID('fa73a202-5642-4cbe-8b1c-4fa6637496b5'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='historylistshow',
            name='show',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recommendation.Show', verbose_name='Show watched'),
        ),
        migrations.AlterField(
            model_name='historylistshow',
            name='type',
            field=models.CharField(default='show', max_length=64),
        ),
        migrations.AlterField(
            model_name='movie',
            name='id',
            field=models.UUIDField(default=uuid.UUID('da1af249-f8c9-4ab5-940f-2a9d9b3480f8'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='show',
            name='id',
            field=models.UUIDField(default=uuid.UUID('c4f4f380-7181-4c15-b406-50b41bc68d29'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='watchlistmovie',
            name='id',
            field=models.UUIDField(default=uuid.UUID('1be124a6-9011-4152-ae20-8d25d54a265b'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='watchlistshow',
            name='id',
            field=models.UUIDField(default=uuid.UUID('f374f453-da98-4899-bd7d-b11fbfea3c8a'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='watchlistshow',
            name='show',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recommendation.Show', verbose_name='Show watched'),
        ),
        migrations.AlterField(
            model_name='watchlistshow',
            name='type',
            field=models.CharField(default='show', max_length=64),
        ),
    ]