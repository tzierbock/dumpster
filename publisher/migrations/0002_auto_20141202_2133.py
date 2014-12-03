# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publisher', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='id',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='id',
        ),
        migrations.AlterField(
            model_name='category',
            name='label',
            field=models.CharField(max_length=20, serialize=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tag',
            name='label',
            field=models.CharField(max_length=20, serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
