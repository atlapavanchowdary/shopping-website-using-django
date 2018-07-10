# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-07-09 14:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CausualShirt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('photo', models.FileField(blank=True, upload_to='')),
                ('desc', models.TextField(max_length=500)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.PositiveIntegerField()),
                ('availability', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
