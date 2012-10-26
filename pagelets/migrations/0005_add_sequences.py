# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):

        if db.backend_name == 'postgres':
            db.execute("CREATE SEQUENCE pagelets_page_id_seq")
            db.execute("SELECT setval('pagelets_page_id_seq', COALESCE((SELECT MAX(id) FROM pagelets_page) + 1, 1))")
            db.execute("ALTER TABLE pagelets_page ALTER COLUMN id SET DEFAULT nextval('pagelets_page_id_seq')")
            db.execute("CREATE SEQUENCE pagelets_pagelet_id_seq")
            db.execute("SELECT setval('pagelets_pagelet_id_seq', COALESCE((SELECT MAX(id) FROM pagelets_pagelet) + 1, 1))")
            db.execute("ALTER TABLE pagelets_pagelet ALTER COLUMN id SET DEFAULT nextval('pagelets_pagelet_id_seq')")

    def backwards(self, orm):

        if db.backend_name == 'postgres':
            db.execute("ALTER TABLE pagelets_page ALTER COLUMN id DROP DEFAULT")
            db.execute("DROP SEQUENCE pagelets_page_id_seq")
            db.execute("ALTER TABLE pagelets_pagelet ALTER COLUMN id DROP DEFAULT")
            db.execute("DROP SEQUENCE pagelets_pagelet_id_seq")

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
            'Meta': {'ordering': "('title',)", 'object_name': 'Page'},
            'base_template': ('django.db.models.fields.CharField', [], {'default': "'pagelets/view_page.html'", 'max_length': '255', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pagelets_page_created'", 'to': "orm['auth.User']"}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'meta_keywords': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'meta_robots': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pagelets_page_last_modified'", 'to': "orm['auth.User']"}),
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
            'Meta': {'ordering': "('slug',)", 'object_name': 'Pagelet'},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pagelets_pagelet_created'", 'to': "orm['auth.User']"}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'css_classes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pagelets_pagelet_last_modified'", 'to': "orm['auth.User']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'html'", 'max_length': '32'})
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
