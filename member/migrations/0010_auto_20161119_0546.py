# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0009_auto_20161119_0544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='address',
            field=models.TextField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.EmailField(default=b'', max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='post_code',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
    ]
