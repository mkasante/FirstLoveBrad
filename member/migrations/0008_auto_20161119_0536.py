# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0007_auto_20161119_0516'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(unique=True, max_length=200)),
            ],
            options={
                'ordering': ['status'],
            },
        ),
        migrations.AlterField(
            model_name='member',
            name='attendance_status',
            field=models.ForeignKey(to='member.Attendance'),
        ),
    ]
