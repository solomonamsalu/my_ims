from django.urls import path
from . import views
urlpatterns=[
 path('companies/',views.CompanyList.as_view(),name='company_list'),
 path('<int:pk>/company_detail',views.CompanyDetail.as_view(),name='company-detail'),
 path('company_create/',views.CompanyCreate.as_view(),name='company_create'),
 path('<int:pk>/company_update/',views.CompanyUpdate.as_view(),name='company_update'),
 path('<int:pk>/company_delete/',views.CompanyDelete.as_view(),name='company_delete')
]