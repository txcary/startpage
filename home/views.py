from django.shortcuts import render
from home.models import Site
from home.models import Group 

# Create your views here.
def index(request):
    context = {}
    context['groupList'] = []
    siteList = Site.objects.order_by('name').all()
    grpList = Group.objects.order_by('priority').all()
    for grpObj in grpList:
        group = {}
        group['name'] = grpObj.name
        group['siteList'] = []
        for siteObj in siteList:
            if siteObj.group == grpObj.name:
                site = {}
                site['name'] = siteObj.name
                site['url'] = siteObj.url
                site['image'] = siteObj.image
                if site['image'] == "":
                    strList = siteObj.url.split('/')
                    site['image'] = "http://"+strList[2]+"/favicon.ico"
                group['siteList'].append(site)
        context['groupList'].append(group)
    return render(request, "index.html", context)