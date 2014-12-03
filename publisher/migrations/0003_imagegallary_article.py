# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publisher', '0002_auto_20141202_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagegallary',
            name='article',
            field=models.ForeignKey(default=3, to='publisher.Article'),
            preserve_default=False,
        ),
    ]
