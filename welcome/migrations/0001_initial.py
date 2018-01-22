# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50, null=True, verbose_name=b'Email Address', blank=True)),
                ('instagram', models.CharField(max_length=50, null=True, blank=True)),
                ('logo', models.CharField(max_length=1000, blank=True)),
                ('country', models.CharField(max_length=100, blank=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
