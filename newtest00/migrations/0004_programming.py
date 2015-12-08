# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20150527_1555'),
        ('newtest00', '0003_docpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Programming',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pages.Page')),
                ('comments_count', models.IntegerField(default=0, editable=False)),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
                ('add_toc', models.BooleanField(default=False, help_text='Include a list of child links', verbose_name='ADD TOC')),
                ('allow_comments', models.BooleanField(default=False, verbose_name='Allow comments')),
                ('tutorial_url', models.URLField(help_text='Add source of the tutorial', max_length=100, blank=True)),
                ('program_language', models.CharField(help_text='Add programming language of tutorial', max_length=100, blank=True)),
            ],
            options={
                'ordering': ('_order',),
            },
            bases=('pages.page', models.Model),
        ),
    ]
