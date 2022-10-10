from django.contrib import admin

from .models import Supplier
class SupplierAdmin(admin.ModelAdmin):
    list_display=['company','first_name','last_name']
admin.site.register(Supplier,SupplierAdmin)
