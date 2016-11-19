# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0010_auto_20161119_0546'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicInstitution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=200)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AlterField(
            model_name='member',
            name='attendance_status',
            field=models.ForeignKey(related_name='attendance_status', to='member.Attendance'),
        ),
    ]
