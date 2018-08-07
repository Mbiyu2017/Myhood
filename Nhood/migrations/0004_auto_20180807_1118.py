# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-08-07 08:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Nhood', '0003_auto_20180806_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neighbourhood',
            name='occupants',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
