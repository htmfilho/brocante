# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-13 17:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscription', '0009_auto_20170909_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagehistory',
            name='type',
            field=models.CharField(choices=[('SUBMISSION_CONFIRMATION', 'Submission Confirmation'), ('INSCRIPTION_CONFIRMATION', 'Inscription Confirmation'), ('WAITING_LIST', 'Waiting List'), ('INSTRUCTIONS', 'Instructions')], default='INSCRIPTION_CONFIRMATION', max_length=30),
        ),
    ]