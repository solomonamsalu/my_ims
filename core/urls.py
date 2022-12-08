from django.urls import path
from . import views
urlpatterns=[
 path('companies/',views.CompanyList.as_view(),name='company_list'),
 path('company_create/',views.company_create,name='company_create')
]