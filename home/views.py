from django.shortcuts import render
from home.models import Site
from home.models import Group 
from home.models import Search 

# Create your views here.
def index(request):
    context = {}
    context['groupList'] = []
    context['searchList'] = []
    siteList = Site.objects.order_by('name').all()
    searchList = Search.objects.order_by('name').all()
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
    idx = 0
    for searchObj in searchList:
        search = {}
        search['name'] = searchObj.name
        search['urlPartBeforeKeywords'] = searchObj.urlPartBeforeKeywords
        search['urlPartAfterKeywords'] = searchObj.urlPartAfterKeywords
        search['image'] = searchObj.image
        search['id'] = "search"+str(idx)
        idx = idx+1
        if searchObj.image == "":
            strList = searchObj.urlPartBeforeKeywords.split('/')
            search['image'] = "http://"+strList[2]+"/favicon.ico"
        context['searchList'].append(search)
    return render(request, "index.html", context)