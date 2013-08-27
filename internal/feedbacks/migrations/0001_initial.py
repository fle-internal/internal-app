# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Feedback'
        db.create_table(u'feedbacks_feedback', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('maker', self.gf('django.db.models.fields.related.ForeignKey')(related_name='feedbacks_made', to=orm['profiles.TeamMember'])),
            ('target', self.gf('django.db.models.fields.related.ForeignKey')(related_name='feedbacks', to=orm['profiles.TeamMember'])),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(related_name='feedbacks', to=orm['projects.Project'])),
            ('participation_rating', self.gf('django.db.models.fields.IntegerField')()),
            ('participation_rationale', self.gf('django.db.models.fields.TextField')()),
            ('contribution_rating', self.gf('django.db.models.fields.IntegerField')()),
            ('contribution_rationale', self.gf('django.db.models.fields.TextField')()),
            ('communication_rating', self.gf('django.db.models.fields.IntegerField')()),
            ('communication_rationale', self.gf('django.db.models.fields.TextField')()),
            ('ease_of_working_together_rating', self.gf('django.db.models.fields.IntegerField')()),
            ('ease_of_working_together_rationale', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'feedbacks', ['Feedback'])


    def backwards(self, orm):
        # Deleting model 'Feedback'
        db.delete_table(u'feedbacks_feedback')


    models = {
        u'feedbacks.feedback': {
            'Meta': {'object_name': 'Feedback'},
            'communication_rating': ('django.db.models.fields.IntegerField', [], {}),
            'communication_rationale': ('django.db.models.fields.TextField', [], {}),
            'contribution_rating': ('django.db.models.fields.IntegerField', [], {}),
            'contribution_rationale': ('django.db.models.fields.TextField', [], {}),
            'ease_of_working_together_rating': ('django.db.models.fields.IntegerField', [], {}),
            'ease_of_working_together_rationale': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maker': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'feedbacks_made'", 'to': u"orm['profiles.TeamMember']"}),
            'participation_rating': ('django.db.models.fields.IntegerField', [], {}),
            'participation_rationale': ('django.db.models.fields.TextField', [], {}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'feedbacks'", 'to': u"orm['projects.Project']"}),
            'target': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'feedbacks'", 'to': u"orm['profiles.TeamMember']"})
        },
        u'profiles.badges': {
            'Meta': {'object_name': 'Badges'},
            'badge_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
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
        },
        u'projects.project': {
            'Meta': {'object_name': 'Project'},
            'collaborators': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'projects'", 'symmetrical': 'False', 'through': u"orm['projects.Role']", 'to': u"orm['profiles.TeamMember']"}),
            'deadline': ('django.db.models.fields.DateField', [], {'max_length': '10'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '300'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'projects_owned'", 'to': u"orm['profiles.TeamMember']"}),
            'start_date': ('django.db.models.fields.DateField', [], {'max_length': '10'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'projects.role': {
            'Meta': {'object_name': 'Role'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'roles'", 'to': u"orm['profiles.TeamMember']"}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projects.Project']"}),
            'role_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['feedbacks']