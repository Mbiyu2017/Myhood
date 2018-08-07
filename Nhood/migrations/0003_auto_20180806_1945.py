# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-08-06 16:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Nhood', '0002_remove_profile_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neighbourhood',
            name='admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]