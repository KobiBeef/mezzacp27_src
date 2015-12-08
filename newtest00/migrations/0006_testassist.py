# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newtest00', '0005_programming_allow_toc'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestAssist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('topic', models.CharField(max_length=200, blank=True)),
                ('main_tutorial', models.ForeignKey(to='newtest00.Programming')),
            ],
        ),
    ]
