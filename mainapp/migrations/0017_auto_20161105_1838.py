# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-05 18:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0016_applyproject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applyproject',
            name='approval',
            field=models.BooleanField(default=False),
        ),
    ]