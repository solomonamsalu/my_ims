from django.urls import path
from . import views
urlpatterns=[
    path('purchaseorder_list',views.PurchaseorderList.as_view(),name='purchaseorder_list'),
    path('<int:pk>/purchaseorder_detail',views.PurchaseorderDetail.as_view(),name='purchaseorder_detail'),
    path('purchaseorder_create',views.PurchaseorderCreate.as_view(),name='purchaseorder_create'),
    path('<int:pk>/purchaseorder_update',views.PurchaseorderUpdate.as_view(),name='purchaseorder_update'),
    path('<int:pk>/purchaseorder_delete',views.PurchaseorderDelete.as_view(),name='purchaseorder_delete')
]