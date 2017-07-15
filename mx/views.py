# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, render_to_response
import scripts.mx as mx
from nettools.forms import fileForm
from scripts.checkhost import isValidDomain
import json
from django.contrib.auth.decorators import login_required


@login_required
def get(request):
    try:
        domain = request.POST['domain']
        requested = True
    except:
        return render(request, 'mx/index.html')
        requested = False
    if isValidDomain(domain) == False:
        return render(request,'mx/get.html',{'invalid':True,'domain':domain})
    m = mx.getRecord(domain)
    context = {'domain' : domain,
                'flag'  : requested,
                'records' : m
              }
    return render(request,'mx/get.html',context)

@login_required
def index(request):
    try:
        domain = request.POST['domain']
        flag = True
    except:
        flag = False
        return render(request, 'mx/index.html')
    context = {'domain': domain,'flag':flag}
    return render(request,'mx/index.html', context)

@login_required
def getfile(request):
    domains = []

    if request.method == "POST":
        newform = fileForm(request.POST, request.FILES)

        if newform.is_valid():
            print newform.cleaned_data['file_location']
            inputFile = newform.cleaned_data['file_location']
            inputFile.seek(0)
            data = inputFile.read()
            for d in data.split():
                if isValidDomain(d):
                    domains.append(d)
        else:
            newform = fileForm()

    else:
        return render(request, 'mx/index.html')
    if len(domains) == 0:
        return render(request, 'mx/index.html',{'invalid':True})
    dom_json = json.dumps(domains)
    context = {
                'domains'   :domains,
                'dom_json'  :dom_json
               }
    return render(request, 'mx/get_multiple.html',context)
