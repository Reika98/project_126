# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-30 10:14
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orgsite', '0003_auto_20170530_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='venue',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='faqs',
            name='answer',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='organization',
            name='contact',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='organization',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='organization',
            name='mission',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='organization',
            name='phone',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')]),
        ),
        migrations.AlterField(
            model_name='organization',
            name='vision',
            field=models.TextField(),
        ),
    ]
