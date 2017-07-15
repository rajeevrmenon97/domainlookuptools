# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, render_to_response
import scripts.blacklist as bl
from nettools.forms import fileForm
import scripts.checkhost as check
import json
from django.contrib.auth.decorators import login_required


@login_required
def get(request):
    try:
        domain = request.POST['domain']
        requested = True
    except:
        return render(request, 'blacklist/index.html')
        requested = False
    if check.isValidDomain(domain) == False and check.isValidIPv4(domain) == False:
        return render(request,'blacklist/get.html',{'invalid':True,'domain':domain})
    if check.isValidIPv4(domain):
        rec = bl.getRecord(domain, False)
    else:
        rec = bl.getRecord(domain)
    context = {'domain'     : domain,
                'flag'      : requested,
                'records'   : rec
              }
    return render(request,'blacklist/get.html',context)

@login_required
def index(request):
    try:
        domain = request.POST['domain']
        flag = True
    except:
        flag = False
        return render(request, 'blacklist/index.html')
    context = {'domain': domain,'flag':flag}
    return render(request,'blacklist/index.html', context)

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
                if check.isValidDomain(d):
                    domains.append(d)
        else:
            newform = fileForm()

    else:
        return render(request, 'blacklist/index.html')
    if len(domains) == 0:
        return render(request, 'blacklist/index.html',{'invalid':True})
    dom_json = json.dumps(domains)
    context = {
                'domains'   :domains,
                'dom_json'  :dom_json
               }
    return render(request, 'blacklist/get_multiple.html',context)
