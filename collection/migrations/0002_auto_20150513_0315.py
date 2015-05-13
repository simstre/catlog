# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='last_updated',
            field=models.DateTimeField(null=True, default=django.utils.timezone.now),
        ),
    ]
