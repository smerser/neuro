# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'dr'
        db.create_table('main_dr', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ini', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('fnavn', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('enavn', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal('main', ['dr'])

        # Adding model 'patienter'
        db.create_table('main_patienter', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('navn', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('cpr', self.gf('django.db.models.fields.CharField')(unique=True, max_length=11)),
            ('sgpl', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('dr', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.dr'], null=True, blank=True)),
            ('diagnose', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('medicin', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('start', self.gf('django.db.models.fields.DateField')(max_length=11, null=True, blank=True)),
            ('interval', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('seneste', self.gf('django.db.models.fields.DateField')(max_length=11, null=True, blank=True)),
            ('booking', self.gf('django.db.models.fields.DateField')(max_length=11, null=True, blank=True)),
            ('NB', self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True)),
            ('tid_hos', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('active', self.gf('django.db.models.fields.CharField')(default='Active', max_length=10, null=True, blank=True)),
        ))
        db.send_create_signal('main', ['patienter'])


    def backwards(self, orm):
        # Deleting model 'dr'
        db.delete_table('main_dr')

        # Deleting model 'patienter'
        db.delete_table('main_patienter')


    models = {
        'main.dr': {
            'Meta': {'object_name': 'dr'},
            'enavn': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'fnavn': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ini': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'})
        },
        'main.patienter': {
            'Meta': {'object_name': 'patienter'},
            'NB': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'active': ('django.db.models.fields.CharField', [], {'default': "'Active'", 'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'booking': ('django.db.models.fields.DateField', [], {'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'cpr': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '11'}),
            'diagnose': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'dr': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.dr']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interval': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'medicin': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'navn': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'seneste': ('django.db.models.fields.DateField', [], {'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'sgpl': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'start': ('django.db.models.fields.DateField', [], {'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'tid_hos': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['main']