# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-03 15:53
from __future__ import unicode_literals

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(error_messages={'unique': 'A user with that email already exists.'}, help_text='Required. 60 characters or fewer.', max_length=60, unique=True, verbose_name='email')),
                ('is_active', models.BooleanField(default=True, verbose_name='is_active')),
                ('is_superuser', models.IntegerField(default=False)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
