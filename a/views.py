# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, render_to_response
import scripts.a as a
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
        return render(request, 'a/index.html')
        requested = False
    if isValidDomain(domain) == False:
        return render(request,'a/get.html',{'invalid':True,'domain':domain})
    ar = a.getRecord(domain)
    a.out(ar)
    context = {'domain'     : domain,
                'flag'      : requested,
                'records'   : ar
              }
    return render(request,'a/get.html',context)

@login_required
def index(request):
    try:
        domain = request.POST['domain']
        flag = True
    except:
        flag = False
        return render(request, 'a/index.html')
    context = {'domain': domain,'flag':flag}
    return render(request,'a/index.html', context)

@login_required
def getfile(request):
    domains = []

    if request.method == "POST":
        newform = fileForm(request.POST, request.FILES)

        if newform.is_valid():
            inputFile = newform.cleaned_data['file_location']
            inputFile.seek(0)
            data = inputFile.read()
            for d in data.split():
                if isValidDomain(d):
                    domains.append(d)
        else:
            newform = fileForm()

    else:
        return render(request, 'a/index.html')
    if len(domains) == 0:
        return render(request, 'a/index.html',{'invalid':True})
    dom_json = json.dumps(domains)
    context = {
                'domains'   :domains,
                'dom_json'  :dom_json
               }
    return render(request, 'a/get_multiple.html',context)
