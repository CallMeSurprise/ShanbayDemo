# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-05 16:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dict', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cet6',
            name='id',
            field=models.AutoField(auto_created=True, default=10086, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cet6',
            name='word_id',
            field=models.IntegerField(),
        ),
    ]
