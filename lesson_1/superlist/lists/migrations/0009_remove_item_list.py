# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0008_item_note'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='list',
        ),
    ]
