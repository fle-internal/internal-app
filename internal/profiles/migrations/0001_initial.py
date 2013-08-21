# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Badges'
        db.create_table(u'profiles_badges', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('badge_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'profiles', ['Badges'])

        # Adding model 'TeamMember'
        db.create_table(u'profiles_teammember', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=254, db_index=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('is_admin', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('bio', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'profiles', ['TeamMember'])

        # Adding M2M table for field badges on 'TeamMember'
        m2m_table_name = db.shorten_name(u'profiles_teammember_badges')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('teammember', models.ForeignKey(orm[u'profiles.teammember'], null=False)),
            ('badges', models.ForeignKey(orm[u'profiles.badges'], null=False))
        ))
        db.create_unique(m2m_table_name, ['teammember_id', 'badges_id'])

        # Adding model 'Post'
        db.create_table(u'profiles_post', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['profiles.TeamMember'])),
        ))
        db.send_create_signal(u'profiles', ['Post'])


    def backwards(self, orm):
        # Deleting model 'Badges'
        db.delete_table(u'profiles_badges')

        # Deleting model 'TeamMember'
        db.delete_table(u'profiles_teammember')

        # Removing M2M table for field badges on 'TeamMember'
        db.delete_table(db.shorten_name(u'profiles_teammember_badges'))

        # Deleting model 'Post'
        db.delete_table(u'profiles_post')


    models = {
        u'profiles.badges': {
            'Meta': {'object_name': 'Badges'},
            'badge_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'profiles.post': {
            'Meta': {'object_name': 'Post'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profiles.TeamMember']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'profiles.teammember': {
            'Meta': {'object_name': 'TeamMember'},
            'badges': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['profiles.Badges']", 'symmetrical': 'False'}),
            'bio': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '254', 'db_index': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['profiles']