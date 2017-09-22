# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colocaciones', '0003_auto_20170922_0408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oferta',
            name='id',
            field=models.CharField(max_length=20, serialize=False, primary_key=True),
        ),
    ]
