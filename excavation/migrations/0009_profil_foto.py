# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-27 15:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('excavation', '0008_auto_20160827_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='profil',
            name='foto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='excavation.Foto'),
        ),
    ]
