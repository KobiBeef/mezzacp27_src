# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20150527_1555'),
        ('newtest00', '0002_testmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pages.Page')),
                ('comments_count', models.IntegerField(default=0, editable=False)),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
                ('add_toc', models.BooleanField(default=False, help_text='Include a list of child links', verbose_name='ADD TOC')),
                ('allow_comments', models.BooleanField(default=False, verbose_name='Allow comments')),
            ],
            options={
                'ordering': ('_order',),
                'verbose_name': 'Doc Page',
                'verbose_name_plural': 'Doc Pages',
            },
            bases=('pages.page', models.Model),
        ),
    ]
