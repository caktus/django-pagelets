# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers
import taggit.models


class Migration(migrations.Migration):

    dependencies = [
        ('pagelets', '0004_sharedpagelet'),
        ('taggit', '__first__'),
    ]

    operations = [
        migrations.RemoveField('page', 'tags'),
        migrations.AddField(
            model_name='page',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', verbose_name='Tags', to='taggit.Tag', through='taggit.TaggedItem'),
        ),
    ]
