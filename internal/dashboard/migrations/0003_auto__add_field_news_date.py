# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'News.date'
        db.add_column(u'dashboard_news', 'date',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2013, 9, 22, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'News.date'
        db.delete_column(u'dashboard_news', 'date')


    models = {
        u'dashboard.news': {
            'Meta': {'object_name': 'News'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['dashboard']