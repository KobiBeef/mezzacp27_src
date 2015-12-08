# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newtest00', '0006_testassist'),
    ]

    operations = [
        migrations.AddField(
            model_name='programming',
            name='allow_content',
            field=models.BooleanField(default=False, help_text=b'include page content', verbose_name='Show content'),
        ),
    ]
