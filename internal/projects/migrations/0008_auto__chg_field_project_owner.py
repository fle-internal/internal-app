# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Project.owner'
        db.alter_column(u'projects_project', 'owner_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['profiles.TeamMember']))

    def backwards(self, orm):

        # Changing field 'Project.owner'
        db.alter_column(u'projects_project', 'owner_id', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['profiles.TeamMember']))

    models = {
        u'profiles.badges': {
            'Meta': {'object_name': 'Badges'},
            'badge_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'profiles.teammember': {
            'Meta': {'object_name': 'TeamMember'},
            'avatar': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'badges': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['profiles.Badges']", 'symmetrical': 'False'}),
            'bio': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '254', 'db_index': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'github_login': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'projects.project': {
            'Meta': {'unique_together': "(('name', 'github_repo_link'),)", 'object_name': 'Project'},
            'collaborators': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'projects'", 'symmetrical': 'False', 'through': u"orm['projects.Role']", 'to': u"orm['profiles.TeamMember']"}),
            'deadline': ('django.db.models.fields.DateField', [], {'max_length': '10'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '300'}),
            'github_repo_link': ('django.db.models.fields.URLField', [], {'db_index': 'True', 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'projects_owned'", 'null': 'True', 'to': u"orm['profiles.TeamMember']"}),
            'start_date': ('django.db.models.fields.DateField', [], {'max_length': '10'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'projects.role': {
            'Meta': {'object_name': 'Role'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'roles'", 'to': u"orm['profiles.TeamMember']"}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projects.Project']"}),
            'role_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'projects.task': {
            'Meta': {'object_name': 'Task'},
            'assigned': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tasks_assigned'", 'null': 'True', 'to': u"orm['profiles.TeamMember']"}),
            'deadline': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'github_link': ('django.db.models.fields.URLField', [], {'db_index': 'True', 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tasks'", 'null': 'True', 'to': u"orm['projects.Project']"}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'open'", 'max_length': '7'})
        }
    }

    complete_apps = ['projects']