# Generated by Django 4.1.7 on 2023-03-12 16:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 3, 12, 16, 37, 6, 169594, tzinfo=datetime.timezone.utc), verbose_name='Дата создания'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='work',
            name='updated_at',
            field=models.DateField(auto_now=True, verbose_name='Дата обновления'),
        ),
        migrations.AlterField(
            model_name='work',
            name='work_type',
            field=models.CharField(choices=[('dry', 'Химчистка')], max_length=30, verbose_name='Вид работы'),
        ),
    ]
