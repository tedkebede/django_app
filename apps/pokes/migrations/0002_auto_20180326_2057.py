# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-26 20:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokes',
            name='pokes',
            field=models.IntegerField(null=True),
        ),
    ]
