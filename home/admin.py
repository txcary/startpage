from django.contrib import admin
from home.models import Site 
from home.models import Group 
from home.models import Search 

# Register your models here.
class SiteAdmin(admin.ModelAdmin):
    list_display = ["name", "url", "image", "group"]
class SearchAdmin(admin.ModelAdmin):
    list_display = ["name", "image", "urlPartBeforeKeywords", "urlPartAfterKeywords"]
admin.site.register(Site, SiteAdmin)
admin.site.register(Search, SearchAdmin)
admin.site.register(Group)