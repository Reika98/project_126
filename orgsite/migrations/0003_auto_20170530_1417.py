# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-30 06:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orgsite', '0002_auto_20170530_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faqs',
            name='answer',
            field=models.TextField(),
        ),
    ]
