from django.contrib import admin
from .models import Company,Store
class CompanyAdmin(admin.ModelAdmin):
    list_display=['id','name']
    fields=['name']
class StoreAdmin(admin.ModelAdmin):
    list_display=['store_number','company']
admin.site.register(Company,CompanyAdmin)
admin.site.register(Store,StoreAdmin)