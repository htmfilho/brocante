# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-01 15:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscription', '0002_auto_20170729_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscription',
            name='address',
            field=models.TextField(verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='desired_place',
            field=models.TextField(blank=True, null=True, verbose_name='Desired Place'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='last_name',
            field=models.CharField(max_length=30, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='number_places',
            field=models.IntegerField(verbose_name='Places'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='Phone'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='registered',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Registered'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='status',
            field=models.CharField(choices=[('NOT_CONFIRMED', 'Not Confirmed'), ('CONFIRMED', 'Confirmed'), ('WAITING_LIST', 'Waiting List')], default='NOT_CONFIRMED', max_length=20, verbose_name='Status'),
        ),
    ]
