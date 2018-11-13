from django.contrib import admin
from home.models import Site 
from home.models import Group 

# Register your models here.
class SiteAdmin(admin.ModelAdmin):
    list_display = ["name", "url", "image", "group"]
admin.site.register(Site, SiteAdmin)
admin.site.register(Group)