# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0007_auto_20170220_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='note',
            field=models.TextField(default=''),
        ),
    ]
