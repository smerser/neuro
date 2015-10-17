# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import admin
from django import forms
from django.core.mail import send_mail
from django.shortcuts import render_to_response, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse
from django.template import RequestContext
from django.forms.models import modelformset_factory, inlineformset_factory, modelform_factory
from datetime import datetime, timedelta
from django.conf import settings
import subprocess
import re
import json

from django.db.models import F
from reportlab.pdfgen import canvas
from django.http import HttpResponse

from main.models import patienter, dr, patientForm


@login_required
def rapporter(request):
    return render_to_response('rapporter.html',  context_instance=RequestContext(request))



@login_required
def rscript(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    #response['Content-Disposition'] = 'attachment; filename="rapport.pdf"'
    
    pd = request.POST
    
    if pd.get('dl') == 'on':
        ptt = patienter.objects.extra(where=["( (strftime('%%s', booking) - strftime('%%s', seneste)) / 86400) > interval"],)
    else:
        ptt = patienter.objects.all()
    
    if pd.get('ia') == None:
        ptt = ptt.exclude(active="Inactive")
    
    if pd.get('dr'):  
        ptt = ptt.filter(doc=pd.get('dr'))

    if pd.get('dg'):
        ptt = ptt.filter(diagnose=pd.get('dg'))
    
    ## ROW AND COLUMN SETUP
    nl    =  15
    ypos  = 780
    c1pos = 120
    c2pos = c1pos + 150
    c3pos = c2pos +  60
    c4pos = c3pos +  40
    c5pos = c4pos +  80
    
    # Create the PDF object, using the response object as its "file."
    # Draw things on the PDF. Here's where the PDF generation happens.
    p = canvas.Canvas(response)
    
    for x in ptt:
        if ypos == 780:     ## Headers
            p.setFont("Helvetica", 8)
            p.drawString(c1pos, ypos, 'Navn')
            p.drawString(c2pos, ypos, 'CPR')
            p.drawString(c3pos, ypos, 'Lage')
            p.drawString(c4pos, ypos, 'Diagnose')
            p.drawString(c5pos, ypos, 'Booking')
            p.line(120, 770, 500, 770)
            ypos -= 30
        p.drawString(c1pos, ypos, x.navn)
        p.drawString(c2pos, ypos, x.cpr)
        p.drawString(c3pos, ypos, x.doc)
        p.drawString(c4pos, ypos, x.diagnose)
        if not x.gtdl:
            p.setFillColorRGB(255,0,0)  # set font color
            p.drawString(c5pos, ypos, 'For sent')
            p.setFillColorRGB(0,0,0)    # reset font colour
        elif x.gtdl == 'missing':
            p.drawString(c5pos, ypos, 'Info mangler')
        else:
            p.drawString(c5pos, ypos, 'OK')
        ypos -= nl
        if ypos < 80:   ## New page
            p.showPage()
            ypos = 780

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response


'''
@login_required
def rscript(request):
    if request.method == 'GET':
        return HttpResponse('<html><body>No POST data available for report!</body></html>')
    elif request.method == 'POST':
        rapport = 'rapport'
        try:
            postdata = request.POST
            subprocess.call("cd "+settings.RSCRIPTS_PATH+"; cat pageVars.R | sed s/dr_var/'"+str(postdata.get('dr'))+"'/ | sed s/dg_var/'"+str(postdata.get('dg'))+"'/ | sed s/dl_var/'"+str(postdata.get('dl'))+"'/ > tmp.R", shell=True)
            subprocess.call("cd "+settings.RSCRIPTS_PATH+"; R --no-save < tmp.R", shell=True)
            rapport = settings.RSCRIPTS_PATH+rapport+'.pdf'
            f = open(rapport, 'r')
            pdf_content = f.read()
            f.close()
            response = HttpResponse(pdf_content, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename=report'
            return response
        except:
            return HttpResponse('<html><body>'+settings.RSCRIPTS_PATH+'</body></html>')
        return HttpResponseRedirect('/neuro/all/')
'''


@login_required
def show_all(request, all=None):
    if not all:
        a = patienter.objects.filter(active='Active')
    else:
        a = patienter.objects.all()
    a = [{'id': x.id, 'navn': x.navn, 'cpr': x.cpr, 'dr': str(x.dr), 'delay': x.gtdl} for x in a]   ## , 'tid': str(x.booking) ## str(dr.objects.get(pk=x.dr_id))
    a = json.dumps(a)
    return render_to_response('all.html', {'patients': a}, context_instance=RequestContext(request))


@login_required
def show_one(request, id=id):
    a= get_object_or_404(patienter, pk=id)
    frm = patientForm(instance=a)
    if request.method == "POST":
        frm = patientForm(request.POST, instance=a)
        if frm.is_valid():
            frm.save()
    try:
        nxt = a.seneste + timedelta(days=a.interval)
        nxt = str(nxt) + ', uge: ' + nxt.strftime("%W")
    except:
        nxt = ''
    return render_to_response('one.html', {'frm': frm, 'id': id, 'delay': a.gtdl, 'nxt': nxt}, context_instance=RequestContext(request))


@login_required
def add_one(request):
    if request.method == "POST":
        a = patienter.objects.create()
        frm = patientForm(request.POST, instance=a)
        if frm.is_valid():
            frm.save()
            return render_to_response('one.html', {'frm': frm, 'id': a.id}, context_instance=RequestContext(request))
    frm = patientForm()
    return render_to_response('add.html', {'frm': frm}, context_instance=RequestContext(request))


@login_required
def del_one(request, id):
    a = get_object_or_404(patienter, pk=id)
    a.delete()
    return HttpResponseRedirect('/neuro/add/')


@login_required
def get_cpr(request, cpr):
    if re.match(r'^\d{10}$', cpr):
        cpr = re.sub(r'(\d{4}$)', r'-\1', cpr)
    try:
        a = patienter.objects.get(cpr=cpr)
    except:
        return HttpResponseRedirect('/add/')
    return HttpResponseRedirect('/neuro/one/' + str(a.id))


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


def login_page(request):
        if request.user.is_authenticated():
        return HttpResponseRedirect("/neuro/all/")
    message = None
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect("/neuro/all/")
                else:
                    message = "User inactive"
            else:
                message = "Invalid username and/or password"
    else:
        form = LoginForm()
    return render_to_response('login.html', {'message': message, 'form': form}, context_instance=RequestContext(request))
    
    
def logout_page(request):
    logout(request)
    return HttpResponseRedirect("/neuro/")
