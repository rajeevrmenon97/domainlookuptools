from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'home/index.html')

@login_required
def getall(request):
    try:
        domain = request.POST['domain']
        requested = True
    except:
        return render(request, 'home/index.html')
        requested = False

    context = {'domain' : domain,
                'flag'  : requested,
              }
    return render(request,'home/get_multiple.html',context)
