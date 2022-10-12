from django.urls import path
from . import views
urlpatterns=[
    path('items/',views.ItemList.as_view()),
    path('<int:pk>/item_detail',views.ItemDetail.as_view()),
]