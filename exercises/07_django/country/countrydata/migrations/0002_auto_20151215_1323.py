# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-15 11:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('countrydata', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='continent',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='country',
            name='continent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='countries', to='countrydata.Continent'),
        ),
        migrations.AlterOrderWithRespectTo(
            name='continent',
            order_with_respect_to=None,
        ),
        migrations.AlterOrderWithRespectTo(
            name='country',
            order_with_respect_to=None,
        ),
    ]
