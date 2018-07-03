# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-06-05 07:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscription', '0012_auto_20180603_1410'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=30, unique=True)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
        ),
    ]