# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-18 11:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
