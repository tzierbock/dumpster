# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publisher', '0003_imagegallary_article'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='id',
        ),
        migrations.AddField(
            model_name='article',
            name='shortTitle',
            field=models.CharField(default=b'Title', max_length=50, serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
