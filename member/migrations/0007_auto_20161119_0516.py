# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0006_auto_20161116_0808'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='category',
            new_name='attendance_status',
        ),
    ]
