# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0010_item_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='note',
        ),
    ]
