# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pagelets', '0003_inlinepagelet'),
    ]

    operations = [
        migrations.CreateModel(
            name='SharedPagelet',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(default='main', help_text='Specifies the placement of this pagelet on the page.', max_length=32, choices=[('main', 'Main')], verbose_name='content area')),
                ('order', models.SmallIntegerField(help_text='The order in which pagelets should show up on the page. Lower numbers show up first.', blank=True, choices=[(-10, -10), (-9, -9), (-8, -8), (-7, -7), (-6, -6), (-5, -5), (-4, -4), (-3, -3), (-2, -2), (-1, -1), (0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], null=True)),
                ('pagelet', models.ForeignKey(to_field='id', to='pagelets.Pagelet')),
                ('page', models.ForeignKey(to_field='id', to='pagelets.Page')),
            ],
            options={
                'unique_together': set([('pagelet', 'page')]),
                'ordering': ('order',),
            },
            bases=(models.Model,),
        ),
    ]
