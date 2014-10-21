# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('pagelets', '0005_auto_20140709_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inlinepagelet',
            name='area',
            field=models.CharField(default='main', max_length=32, verbose_name='content area', help_text='Specifies the placement of this pagelet on the page.'),
        ),
        migrations.AlterField(
            model_name='inlinepagelet',
            name='page',
            field=models.ForeignKey(related_name='inline_pagelets', to='pagelets.Page'),
        ),
        migrations.AlterField(
            model_name='inlinepagelet',
            name='pagelet_ptr',
            field=models.OneToOneField(auto_created=True, parent_link=True, to='pagelets.Pagelet', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='page',
            name='created_by',
            field=models.ForeignKey(editable=False, related_name='pagelets_page_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='page',
            name='modified_by',
            field=models.ForeignKey(editable=False, related_name='pagelets_page_last_modified', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='pageattachment',
            name='page',
            field=models.ForeignKey(related_name='attachments', to='pagelets.Page'),
        ),
        migrations.AlterField(
            model_name='pagelet',
            name='created_by',
            field=models.ForeignKey(editable=False, related_name='pagelets_pagelet_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='pagelet',
            name='modified_by',
            field=models.ForeignKey(editable=False, related_name='pagelets_pagelet_last_modified', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='pagelet',
            name='type',
            field=models.CharField(default='html', max_length=32, verbose_name='content type', help_text="Controls the markup language and, in some cases, the JavaScript editor to be used for this pagelet's content."),
        ),
        migrations.AlterField(
            model_name='sharedpagelet',
            name='area',
            field=models.CharField(default='main', max_length=32, verbose_name='content area', help_text='Specifies the placement of this pagelet on the page.'),
        ),
        migrations.AlterField(
            model_name='sharedpagelet',
            name='page',
            field=models.ForeignKey(related_name='shared_pagelets', to='pagelets.Page'),
        ),
    ]
