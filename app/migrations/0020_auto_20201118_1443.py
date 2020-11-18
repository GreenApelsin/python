# Generated by Django 2.2.16 on 2020-11-18 11:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_auto_20201118_1410'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='file',
        ),
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 11, 18, 14, 43, 51, 537557), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 11, 18, 14, 43, 51, 538557), verbose_name='Дата'),
        ),
    ]