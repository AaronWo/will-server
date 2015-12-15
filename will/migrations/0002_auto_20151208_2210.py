# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('will', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='will',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='will',
            name='update_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
