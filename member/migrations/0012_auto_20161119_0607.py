# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0011_auto_20161119_0603'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='study_place',
        ),
        migrations.AddField(
            model_name='member',
            name='academic_institution',
            field=models.ForeignKey(related_name='academic_institution', blank=True, to='member.AcademicInstitution', null=True),
        ),
    ]
