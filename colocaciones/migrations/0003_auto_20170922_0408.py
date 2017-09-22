# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colocaciones', '0002_auto_20170914_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleo',
            name='empresa',
            field=models.ForeignKey(blank=True, to='colocaciones.Empresa', null=True),
        ),
        migrations.AlterField(
            model_name='empleo',
            name='oferta',
            field=models.ForeignKey(blank=True, to='colocaciones.Oferta', null=True),
        ),
        migrations.AlterField(
            model_name='empleo',
            name='persona',
            field=models.ForeignKey(blank=True, to='colocaciones.Persona', null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='rubro',
            field=models.ForeignKey(blank=True, to='colocaciones.Rubro', null=True),
        ),
        migrations.AlterField(
            model_name='oferta',
            name='empresa',
            field=models.ForeignKey(blank=True, to='colocaciones.Empresa', null=True),
        ),
        migrations.AlterField(
            model_name='oferta',
            name='necesidad',
            field=models.ForeignKey(blank=True, to='colocaciones.Rubro', null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='tipoDeTrabajoQuePuedeRealizar',
            field=models.ForeignKey(blank=True, to='colocaciones.Rubro', null=True),
        ),
    ]
