from django.urls import path
from . import views
urlpatterns=[
    # path('item_create',views.ItemCreate.as_view()),
    # url(r'form', views.AddItemForm, name='form'),
    path('items/',views.ItemList.as_view(),name="item_list"),
    path('<int:pk>/item_detail',views.ItemDetail.as_view(),name='item_detail'),
    path('index/',views.index),
    path('item_create/',views.ItemCreate.as_view(),name='item_create'),
    path('<int:pk>/item_update/',views.ItemUpdate.as_view(),name="item_update"),
    path('<int:pk>/item_delete/',views.ItemDelete.as_view(),name='item_delete'),
    path('suppliers/',views.SupplierList.as_view(),name='supplier_list '),
    path('<int:pk>/supplier_detail/',views.SupplierDetail.as_view(),name='supplier-detail'),
    path('supplier_create/',views.SupplierCreate.as_view(),name='supplier_create'),
    path('<int:pk>/supplier_update/',views.SupplierUpdate.as_view(),name="supplier_update"),
    path('<int:pk>/supplier_delete/',views.SupplierDelete.as_view(),name='supplier_delete'),
    
]
