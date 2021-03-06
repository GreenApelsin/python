# Generated by Django 2.2.16 on 2020-11-18 11:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_auto_20201118_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='fileFILE',
            field=models.FileField(default='123.png', upload_to='', verbose_name='Путь к файлу'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 11, 18, 14, 44, 23, 767613), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 11, 18, 14, 44, 23, 768660), verbose_name='Дата'),
        ),
    ]
