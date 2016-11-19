# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0005_member_study_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='course',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='member',
            name='date_of_birth',
            field=models.DateField(null=True, blank=True),
        ),
    ]
