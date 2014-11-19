# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import pagelets.validators
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('creation_date', models.DateTimeField(verbose_name='creation date', auto_now_add=True)),
                ('last_changed', models.DateTimeField(verbose_name='last changed', auto_now=True)),
                ('title', models.CharField(verbose_name='title', help_text="The page title.  To be displayed in the browser's title bar as well as at the top of the page.", max_length=255)),
                ('slug', models.CharField(unique=True, verbose_name='slug', max_length=255, help_text="A short string that uniquely identifies this page. It's used in the page URL, so don't change it unless you're positive nothing links to this page. Valid url chars include uppercase and lowercase letters, decimal digits, hyphen, period, underscore, and tilde. Do not include leading or trailing slashes.", validators=[pagelets.validators.validate_url_chars, pagelets.validators.validate_leading_slash, pagelets.validators.validate_trailing_slash])),
                ('description', models.TextField(blank=True, verbose_name='description', help_text='A description of the page for use in the meta tags and teaser or other short excepts')),
                ('base_template', models.CharField(blank=True, default='pagelets/view_page.html', verbose_name='base template', help_text='Specify an alternative layout template to use for this page.  Clear the selection to use the default layout.', max_length=255)),
                ('meta_keywords', models.CharField(blank=True, verbose_name='meta keywords', help_text='A comma delineated list of keywords', max_length=200)),
                ('meta_robots', models.CharField(blank=True, verbose_name='meta Robots', choices=[('FOLLOW, INDEX', 'FOLLOW, INDEX'), ('NOFOLLOW, NOINDEX', 'NOFOLLOW, NOINDEX'), ('FOLLOW, NOINDEX', 'FOLLOW, NOINDEX'), ('NOFOLLOW, INDEX', 'NOFOLLOW, INDEX')], max_length=20)),
                ('created_by', models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL, related_name='pagelets_page_created')),
                ('modified_by', models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL, related_name='pagelets_page_last_modified')),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', verbose_name='Tags', through='taggit.TaggedItem', help_text='A comma-separated list of tags.')),
            ],
            options={
                'ordering': ('title',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PageAttachment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='attachments/pages/')),
                ('order', models.SmallIntegerField(blank=True, choices=[(-10, -10), (-9, -9), (-8, -8), (-7, -7), (-6, -6), (-5, -5), (-4, -4), (-3, -3), (-2, -2), (-1, -1), (0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], null=True)),
                ('page', models.ForeignKey(related_name='attachments', to='pagelets.Page')),
            ],
            options={
                'ordering': ('order',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pagelet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('creation_date', models.DateTimeField(verbose_name='creation date', auto_now_add=True)),
                ('last_changed', models.DateTimeField(verbose_name='last changed', auto_now=True)),
                ('slug', models.CharField(blank=True, max_length=255, verbose_name='slug', help_text="A short string with no spaces or special characters that uniquely identifies this pagelet.  It may be used to link to load this pagelet dynamically from other places on the site, so don't change it unless you're positive nothing depends on the current name.", null=True)),
                ('css_classes', models.CharField(blank=True, verbose_name='CSS classes', help_text='Extra CSS classes, if any, to be added to the pagelet DIV in the HTML.', max_length=255)),
                ('type', models.CharField(default='html', verbose_name='content type', help_text="Controls the markup language and, in some cases, the JavaScript editor to be used for this pagelet's content.", max_length=32)),
                ('content', models.TextField(blank=True, verbose_name='content')),
            ],
            options={
                'ordering': ('slug',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='InlinePagelet',
            fields=[
                ('pagelet_ptr', models.OneToOneField(auto_created=True, serialize=False, to='pagelets.Pagelet', parent_link=True, primary_key=True)),
                ('area', models.CharField(default='main', verbose_name='content area', help_text='Specifies the placement of this pagelet on the page.', max_length=32)),
                ('order', models.SmallIntegerField(blank=True, choices=[(-10, -10), (-9, -9), (-8, -8), (-7, -7), (-6, -6), (-5, -5), (-4, -4), (-3, -3), (-2, -2), (-1, -1), (0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], help_text='The order in which pagelets should show up on the page. Lower numbers show up first.', null=True)),
                ('page', models.ForeignKey(related_name='inline_pagelets', to='pagelets.Page')),
            ],
            options={
                'ordering': ('order',),
            },
            bases=('pagelets.pagelet', models.Model),
        ),
        migrations.CreateModel(
            name='SharedPagelet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('area', models.CharField(default='main', verbose_name='content area', help_text='Specifies the placement of this pagelet on the page.', max_length=32)),
                ('order', models.SmallIntegerField(blank=True, choices=[(-10, -10), (-9, -9), (-8, -8), (-7, -7), (-6, -6), (-5, -5), (-4, -4), (-3, -3), (-2, -2), (-1, -1), (0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], help_text='The order in which pagelets should show up on the page. Lower numbers show up first.', null=True)),
                ('page', models.ForeignKey(related_name='shared_pagelets', to='pagelets.Page')),
                ('pagelet', models.ForeignKey(to='pagelets.Pagelet')),
            ],
            options={
                'ordering': ('order',),
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='sharedpagelet',
            unique_together=set([('pagelet', 'page')]),
        ),
        migrations.AddField(
            model_name='pagelet',
            name='created_by',
            field=models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL, related_name='pagelets_pagelet_created'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pagelet',
            name='modified_by',
            field=models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL, related_name='pagelets_pagelet_last_modified'),
            preserve_default=True,
        ),
    ]
