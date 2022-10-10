from django.contrib import admin

from .models import Supplier,Item
class SupplierAdmin(admin.ModelAdmin):
    list_display=['company','first_name','last_name']
admin.site.register(Supplier,SupplierAdmin)
class ItemAdmin(admin.ModelAdmin):
    list_display= ['name']
admin.site.register(Item,ItemAdmin)