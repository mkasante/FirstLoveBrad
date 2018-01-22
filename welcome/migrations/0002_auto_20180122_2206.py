# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='logo',
            field=models.CharField(help_text=b'Link to image to use e.g. instagram logo url', max_length=1000, blank=True),
        ),
    ]
