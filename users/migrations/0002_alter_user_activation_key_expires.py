# Generated by Django 3.2.7 on 2021-09-20 11:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 22, 11, 36, 52, 97420, tzinfo=utc)),
        ),
    ]
