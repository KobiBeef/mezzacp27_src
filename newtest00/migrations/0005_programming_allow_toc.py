# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newtest00', '0004_programming'),
    ]

    operations = [
        migrations.AddField(
            model_name='programming',
            name='allow_toc',
            field=models.BooleanField(default=False, help_text='include a side bar of toc', verbose_name='Add assist toc'),
        ),
    ]
