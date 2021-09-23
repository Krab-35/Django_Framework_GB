# Generated by Django 3.2.7 on 2021-09-20 11:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_activation_key_expires'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='возраст'),
        ),
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 22, 11, 38, 6, 490963, tzinfo=utc)),
        ),
    ]