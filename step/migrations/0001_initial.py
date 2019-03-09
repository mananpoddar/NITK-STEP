# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-09 05:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='comingEvents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='documents/')),
                ('title', models.CharField(max_length=80)),
                ('description', models.TextField()),
                ('details', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='govtProjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='documents/')),
                ('title', models.CharField(max_length=80)),
                ('description', models.TextField()),
                ('details', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ongoingProgrammes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='documents/')),
                ('title', models.CharField(max_length=80)),
                ('description', models.TextField()),
                ('details', models.TextField()),
            ],
        ),
    ]
