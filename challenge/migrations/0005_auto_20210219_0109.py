# Generated by Django 3.1.6 on 2021-02-18 16:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0004_auto_20210219_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='start_date',
            field=models.DateField(default=datetime.date.today, verbose_name='시작일'),
        ),
    ]