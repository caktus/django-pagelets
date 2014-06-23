# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import pagelets.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='creation date')),
                ('created_by', models.ForeignKey(to_field='id', to=settings.AUTH_USER_MODEL, editable=False)),
                ('last_changed', models.DateTimeField(auto_now=True, verbose_name='last changed')),
                ('modified_by', models.ForeignKey(to_field='id', to=settings.AUTH_USER_MODEL, editable=False)),
                ('title', models.CharField(help_text="The page title.  To be displayed in the browser's title bar as well as at the top of the page.", max_length=255, verbose_name='title')),
                ('slug', models.CharField(validators=[pagelets.validators.validate_url_chars, pagelets.validators.validate_leading_slash, pagelets.validators.validate_trailing_slash], help_text="A short string that uniquely identifies this page. It's used in the page URL, so don't change it unless you're positive nothing links to this page. Valid url chars include uppercase and lowercase letters, decimal digits, hyphen, period, underscore, and tilde. Do not include leading or trailing slashes.", unique=True, max_length=255, verbose_name='slug')),
                ('description', models.TextField(help_text='A description of the page for use in the meta tags and teaser or other short excepts', blank=True, verbose_name='description')),
                ('base_template', models.CharField(default='pagelets/view_page.html', help_text='Specify an alternative layout template to use for this page.  Clear the selection to use the default layout.', max_length=255, blank=True, verbose_name='base template')),
                ('meta_keywords', models.CharField(help_text='A comma delineated list of keywords', max_length=200, blank=True, verbose_name='meta keywords')),
                ('meta_robots', models.CharField(max_length=20, blank=True, choices=[('FOLLOW, INDEX', 'FOLLOW, INDEX'), ('NOFOLLOW, NOINDEX', 'NOFOLLOW, NOINDEX'), ('FOLLOW, NOINDEX', 'FOLLOW, NOINDEX'), ('NOFOLLOW, INDEX', 'NOFOLLOW, INDEX')], verbose_name='meta Robots')),
                ('tags', models.CharField(default='', max_length=255, blank=True)),
            ],
            options={
                'ordering': ('title',),
            },
            bases=(models.Model,),
        ),
    ]
