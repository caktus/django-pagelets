# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('pagelets', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PageAttachment',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('page', models.ForeignKey(to_field='id', to='pagelets.Page')),
                ('name', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='attachments/pages/')),
                ('order', models.SmallIntegerField(null=True, blank=True, choices=[(-10, -10), (-9, -9), (-8, -8), (-7, -7), (-6, -6), (-5, -5), (-4, -4), (-3, -3), (-2, -2), (-1, -1), (0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)])),
            ],
            options={
                'ordering': ('order',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pagelet',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='creation date')),
                ('created_by', models.ForeignKey(to_field='id', to=settings.AUTH_USER_MODEL, editable=False)),
                ('last_changed', models.DateTimeField(auto_now=True, verbose_name='last changed')),
                ('modified_by', models.ForeignKey(to_field='id', to=settings.AUTH_USER_MODEL, editable=False)),
                ('slug', models.CharField(null=True, help_text="A short string with no spaces or special characters that uniquely identifies this pagelet.  It may be used to link to load this pagelet dynamically from other places on the site, so don't change it unless you're positive nothing depends on the current name.", max_length=255, blank=True, verbose_name='slug')),
                ('css_classes', models.CharField(help_text='Extra CSS classes, if any, to be added to the pagelet DIV in the HTML.', max_length=255, blank=True, verbose_name='CSS classes')),
                ('type', models.CharField(default='html', help_text="Controls the markup language and, in some cases, the JavaScript editor to be used for this pagelet's content.", max_length=32, choices=[('html', 'HTML'), ('markdown', 'Markdown'), ('wymeditor', 'WYMeditor'), ('textile', 'Textile')], verbose_name='content type')),
                ('content', models.TextField(blank=True, verbose_name='content')),
            ],
            options={
                'ordering': ('slug',),
            },
            bases=(models.Model,),
        ),
    ]
