# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eventtype',
            options={'ordering': ['name']},
        ),
        migrations.RenameField(
            model_name='event',
            old_name='atendance_count',
            new_name='attendance_count',
        ),
    ]
