# Generated by Django 3.1.2 on 2020-10-25 01:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='link',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='title',
            field=models.CharField(default=datetime.date(2020, 10, 25), max_length=200),
            preserve_default=False,
        ),
    ]