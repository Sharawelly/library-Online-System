# Generated by Django 5.0.6 on 2024-05-22 12:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 5, 22, 15, 37, 14, 661372), verbose_name='Publishing Date'),
        ),
    ]
