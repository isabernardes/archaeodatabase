# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-27 15:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excavation', '0011_auto_20160827_1747'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profil',
            name='foto',
        ),
        migrations.AddField(
            model_name='foto',
            name='profil',
            field=models.ManyToManyField(blank=True, to='excavation.Profil'),
        ),
    ]
