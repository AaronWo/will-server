# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('will', '0003_auto_20151208_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moment',
            name='create_date',
            field=models.DateTimeField(),
        ),
    ]
