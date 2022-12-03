from django.urls import path
from . import views
urlpatterns=[
    # path('item_create',views.ItemCreate.as_view()),
    # url(r'form', views.AddItemForm, name='form'),
    path('items/',views.ItemList.as_view(),name="items"),
    path('<int:pk>/item_detail',views.ItemDetail.as_view()),
    path('index/',views.index),
    path('item_create/',views.itemcreate)
    
]
