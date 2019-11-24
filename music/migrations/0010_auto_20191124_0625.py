# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-11-24 06:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0009_auto_20191124_0538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='choices',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='question',
            name='gform',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='music.Gform'),
        ),
        migrations.AlterField(
            model_name='question',
            name='ques_type',
            field=models.CharField(choices=[('multiline', 'Multi Line Text'), ('number', 'Number'), ('url', 'URL'), ('checkbox', 'Checkbox'), ('dropdown', 'Dropdown')], default='multiline', max_length=50),
        ),
    ]
