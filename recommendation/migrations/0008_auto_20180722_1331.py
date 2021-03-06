# Generated by Django 2.0.7 on 2018-07-22 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0007_auto_20180722_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historylistshow',
            name='episode',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recommendation.Episode', verbose_name='Episode watched'),
        ),
        migrations.AlterField(
            model_name='show',
            name='tvrage_id',
            field=models.IntegerField(default='1234'),
            preserve_default=False,
        ),
    ]
