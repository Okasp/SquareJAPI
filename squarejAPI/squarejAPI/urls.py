"""squarejAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.urls.conf import include
from rest_framework import views
from api.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/employee', EmployeeList.as_view()),
    path('api/employee/<int:pk>', EmployeeDetail.as_view()),

    path('api/jobs', OrderJobList.as_view()),
    path('api/jobs/<int:pk>', OrderJobDetail.as_view()),
    path('api/employee/jobs/<int:pk>', EmployeeJobList.as_view()),
    path('api/customer', CustomerList.as_view()),
    path('api/customer/<str:pk>', CustomerDetail.as_view()),
    path('api/products', ProductList.as_view()),
    path('api/products/search/<str:search>', ProductSearch.as_view()),
    path('api/products/<int:pk>', ProductDetail.as_view()),
    path('api/store', StoreList.as_view()),
    path('api/store/<str:pk>', StoreDetail.as_view()),
    path('api/warehouse', WarehouseList.as_view()),
    path('api/warehouse/<str:pk>', WarehouseDetail.as_view()),
    path('api/inventory', LocationInventory.as_view()),
    path('api/stockord', StockOrd.as_view()),
    path('api/stockord/<int:pk>', StockOrdDetail.as_view()),
    path('api/customerord', CustomerOrd.as_view()),
    path('api/customerord/<int:pk>', CustomerOrdDetail.as_view()),
    path('api/customerord/job/<int:pk>', OrderJobDetail.as_view()),
    path('api/account', AccountList.as_view()),
    path('api/account/<str:pk>', AccountDetail.as_view()),
    path('api/shipment', ShipmentList.as_view()),
    path('api/shipment/<str:pk>', ShipmentDetail.as_view()),
    path('api/shipment/For_Order_ID/<str:pk>', ShipbyordID.as_view()),
    path('api/shipment/For_Order_ID/<str:pk>', ShipbyordID.as_view()),
    path('api/auth', Auth.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
