from django.db import models
from django.forms import ModelForm
from datetime import date
from django.contrib.auth.models import User


class dr(models.Model):
    ini   = models.CharField(max_length=16, null=True, blank=True)
    fnavn = models.CharField(max_length=50, null=True, blank=True)
    enavn = models.CharField(max_length=50, null=True, blank=True)
    def __unicode__(self):
        return self.ini

class patienter(models.Model):
    navn     = models.CharField(max_length=200)
    cpr      = models.CharField('CPR', null=False, max_length=11, unique=True)
    sgpl     = models.CharField('Sygeplejerske', max_length=200, null=True, blank=True)
    dr       = models.ForeignKey('dr', blank=True, null=True)
    #doc      = models.CharField('Lage', max_length=200, null=True, blank=True)
    diagnose = models.CharField(max_length=200, null=True, blank=True)
    medicin  = models.CharField(max_length=200, null=True, blank=True)
    start    = models.DateField(max_length=11, null=True, blank=True)
    interval = models.PositiveIntegerField(null=True, blank=True)
    seneste  = models.DateField(max_length=11, null=True, blank=True)
    booking  = models.DateField(max_length=11, null=True, blank=True)
    NB       = models.CharField(max_length=512, null=True, blank=True)
    tid_hos  = models.CharField(max_length=200, null=True, blank=True)
    
    STATE=(
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )
    active   = models.CharField('Status', max_length=10, null=True, blank=True, choices=STATE, default='Active')
    
    @property
    def gtdl(self):
        if self.booking is None or self.seneste is None or self.interval is None:
            return 'missing'
        else:
            delta =(self.booking - self.seneste).days
            print delta
            return (delta > 0) and (delta < self.interval) and (self.booking > date.today())


class patientForm(ModelForm):
    class Meta:
        model = patienter

class patientFormShort(ModelForm):
    class Meta:
        model = patienter
        fields = ['id', 'navn', 'cpr', 'interval', 'seneste', 'booking']
        
        

