from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('shops/', views.ShopList.as_view(), name='shop_list'),
    path('shops/<int:pk>', views.ShopDetail.as_view(), name='shop_detail'),
    path('donuts/', views.DonutList.as_view(), name='donut_list'),
    path('donuts/<int:pk>', views.DonutDetail.as_view(), name='donut_detail')

]
