from django.urls import path
from . import views
urlpatterns=[
    path('salesorder_list',views.SalesorderList.as_view(),name='salesorder_list'),
    path('<int:pk>/salesorder_detail',views.SalesorderDetail.as_view(),name='salesorder_detail'),
    path('salesorder_create',views.SalesorderCreate.as_view(),name='salesorder_create'),
    path('<int:pk>/salesorder_update',views.SalesorderUpdate.as_view(),name='salesorder_update'),
    path('<int:pk>/salesorder_delete',views.SalesorderDelete.as_view(),name='salesorderder_delete'),
    path('customer_list/',views.CustomerList.as_view(),name='customer_list'),
    path('<int:pk>/customer_detail/',views.CustomerDetail.as_view(),name='customer_detail'),
    path('customer_create/',views.CustomerCreate.as_view(),name='customer_create'),
    path('<int:pk>/customer_update/',views.CustomerUpdate.as_view(),name='customer_update'),
    path('<int:pk>/customer_delete/',views.CustomerDelete.as_view(),name='customer_delete')
]