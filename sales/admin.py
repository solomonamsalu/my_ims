from django.contrib import admin

from .models import Customer,SalesOrder
admin.site.register(Customer)
admin.site.register(SalesOrder)
