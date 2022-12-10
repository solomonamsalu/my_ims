from django.urls import path
from . import views
urlpatterns=[
 path('companies/',views.CompanyList.as_view(),name='company_list'),
 path('<int:pk>/company_detail',views.CompanyDetail.as_view(),name='company-detail'),
 path('company_create/',views.CompanyCreate.as_view(),name='company_create'),
 path('<int:pk>/company_update/',views.CompanyUpdate.as_view(),name='company_update'),
 path('<int:pk>/company_delete/',views.CompanyDelete.as_view(),name='company_delete'),
 path('stores/',views.StoreList.as_view(),name='store_list'),
 path('<int:pk>/store_detail',views.StoreDetail.as_view(),name='store-detail'),
 path('store_create/',views.StoreCreate.as_view(),name='store_create'),
 path('<int:pk>/store_update/',views.StoreUpdate.as_view(),name='store_update'),
 path('<int:pk>/store_delete/',views.StoreDelete.as_view(),name='store_delete')
]