# Generated by Django 4.2.4 on 2023-12-19 21:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flightsapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='arrival',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 19, 21, 5, 55, 64893)),
        ),
        migrations.AddField(
            model_name='flight',
            name='departure',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 19, 21, 5, 55, 64867)),
        ),
    ]
