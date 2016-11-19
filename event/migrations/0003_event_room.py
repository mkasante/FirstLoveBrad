# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_auto_20161119_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='room',
            field=models.CharField(default=b'', max_length=100),
        ),
    ]
