# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'PageletBase'
        db.create_table('pagelets_pageletbase', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='pagelets_created', to=orm['auth.User'])),
            ('last_changed', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='pagelets_last_modified', to=orm['auth.User'])),
        ))
        db.send_create_signal('pagelets', ['PageletBase'])

        # Adding model 'Page'
        db.create_table('pagelets_page', (
            ('pageletbase_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['pagelets.PageletBase'], unique=True, primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('base_template', self.gf('django.db.models.fields.CharField')(default='pagelets/view_page.html', max_length=255, blank=True)),
            ('meta_keywords', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('meta_robots', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
        ))
        db.send_create_signal('pagelets', ['Page'])

        # Adding model 'Pagelet'
        db.create_table('pagelets_pagelet', (
            ('pageletbase_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['pagelets.PageletBase'], unique=True, primary_key=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('css_classes', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(default='html', max_length=32)),
            ('content', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('pagelets', ['Pagelet'])

        # Adding model 'InlinePagelet'
        db.create_table('pagelets_inlinepagelet', (
            ('pagelet_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['pagelets.Pagelet'], unique=True, primary_key=True)),
            ('area', self.gf('django.db.models.fields.CharField')(default='main', max_length=32)),
            ('order', self.gf('django.db.models.fields.SmallIntegerField')(null=True, blank=True)),
            ('page', self.gf('django.db.models.fields.related.ForeignKey')(related_name='inline_pagelets', to=orm['pagelets.Page'])),
        ))
        db.send_create_signal('pagelets', ['InlinePagelet'])

        # Adding model 'SharedPagelet'
        db.create_table('pagelets_sharedpagelet', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('area', self.gf('django.db.models.fields.CharField')(default='main', max_length=32)),
            ('order', self.gf('django.db.models.fields.SmallIntegerField')(null=True, blank=True)),
            ('pagelet', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pagelets.Pagelet'])),
            ('page', self.gf('django.db.models.fields.related.ForeignKey')(related_name='shared_pagelets', to=orm['pagelets.Page'])),
        ))
        db.send_create_signal('pagelets', ['SharedPagelet'])

        # Adding unique constraint on 'SharedPagelet', fields ['pagelet', 'page']
        db.create_unique('pagelets_sharedpagelet', ['pagelet_id', 'page_id'])

        # Adding model 'PageAttachment'
        db.create_table('pagelets_pageattachment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('page', self.gf('django.db.models.fields.related.ForeignKey')(related_name='attachments', to=orm['pagelets.Page'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('order', self.gf('django.db.models.fields.SmallIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('pagelets', ['PageAttachment'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'SharedPagelet', fields ['pagelet', 'page']
        db.delete_unique('pagelets_sharedpagelet', ['pagelet_id', 'page_id'])

        # Deleting model 'PageletBase'
        db.delete_table('pagelets_pageletbase')

        # Deleting model 'Page'
        db.delete_table('pagelets_page')

        # Deleting model 'Pagelet'
        db.delete_table('pagelets_pagelet')

        # Deleting model 'InlinePagelet'
        db.delete_table('pagelets_inlinepagelet')

        # Deleting model 'SharedPagelet'
        db.delete_table('pagelets_sharedpagelet')

        # Deleting model 'PageAttachment'
        db.delete_table('pagelets_pageattachment')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'pagelets.inlinepagelet': {
            'Meta': {'ordering': "('order',)", 'object_name': 'InlinePagelet', '_ormbases': ['pagelets.Pagelet']},
            'area': ('django.db.models.fields.CharField', [], {'default': "'main'", 'max_length': '32'}),
            'order': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inline_pagelets'", 'to': "orm['pagelets.Page']"}),
            'pagelet_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['pagelets.Pagelet']", 'unique': 'True', 'primary_key': 'True'})
        },
        'pagelets.page': {
            'Meta': {'ordering': "('title',)", 'object_name': 'Page', '_ormbases': ['pagelets.PageletBase']},
            'base_template': ('django.db.models.fields.CharField', [], {'default': "'pagelets/view_page.html'", 'max_length': '255', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'meta_keywords': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'meta_robots': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'pageletbase_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['pagelets.PageletBase']", 'unique': 'True', 'primary_key': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'pagelets.pageattachment': {
            'Meta': {'ordering': "('order',)", 'object_name': 'PageAttachment'},
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'attachments'", 'to': "orm['pagelets.Page']"})
        },
        'pagelets.pagelet': {
            'Meta': {'ordering': "('slug',)", 'object_name': 'Pagelet', '_ormbases': ['pagelets.PageletBase']},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'css_classes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'pageletbase_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['pagelets.PageletBase']", 'unique': 'True', 'primary_key': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'html'", 'max_length': '32'})
        },
        'pagelets.pageletbase': {
            'Meta': {'object_name': 'PageletBase'},
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pagelets_created'", 'to': "orm['auth.User']"}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pagelets_last_modified'", 'to': "orm['auth.User']"})
        },
        'pagelets.sharedpagelet': {
            'Meta': {'ordering': "('order',)", 'unique_together': "(('pagelet', 'page'),)", 'object_name': 'SharedPagelet'},
            'area': ('django.db.models.fields.CharField', [], {'default': "'main'", 'max_length': '32'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'shared_pagelets'", 'to': "orm['pagelets.Page']"}),
            'pagelet': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pagelets.Pagelet']"})
        }
    }

    complete_apps = ['pagelets']
