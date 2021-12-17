from typing import List
from django.db.models import deletion, manager
from django.http import response
from django.shortcuts import render
from rest_framework.serializers import Serializer

from api.apps import ApiConfig
from .serializers import *
from .models import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class EmployeeList(APIView):
    def get(self, request, format=None):
        employees = Employee.objects.all()
        ser = EmployeeSerializer(employees, many=True)
        return Response (ser.data)

    def post(self, request, format=None):
        ser = EmployeeSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response (ser.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeeDetail(APIView):

    def get(self, request, pk, format=None):
        emp = Employee.objects.get(pk = pk)
        ser = EmployeeSerializer(emp)
        return Response(ser.data)

    def put(self, request, pk, format=None):
        emp = Employee.objects.filter(pk=pk).first()
        ser = EmployeeSerializer(emp, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response (ser.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        emp = Employee.objects.filter(pk=pk)
        emp.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class EmployeeJobList(APIView):
    def get(self, request, pk, format=None):
        jobs = Assigned_To.objects.filter(employee_id = pk)
        ser = Assigned_ToSerializer(jobs, many=True)
        return Response(ser.data)

class OrderJobList(APIView):
    def get(self, request, format=None):
        jobs = Assigned_To.objects.all()
        ser = Assigned_ToSerializer(jobs, many=True)
        return Response (ser.data)

    def post(self, request, format=None):
        ser = Assigned_ToSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response (ser.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderJobDetail(APIView):
    def get(self, request, pk, format=None):
        job = Assigned_To.objects.filter(pk=pk)
        ser = Assigned_ToSerializer(job, many=True)
        return Response(ser.data)
    
    def put(self, request, pk, format=None):
        job = Assigned_To.objects.filter(pk=pk).first()
        ser = Assigned_ToSerializer(job, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response (ser.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        job = Assigned_To.objects.filter(pk=pk).first()
        job.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CustomerList(APIView):
    def get(self, request, format=None):
        custs = Customer.objects.all()
        ser = CustomerSerializer(custs, many=True)
        return Response (ser.data)

    def post(self, request, format=None):
        ser = CustomerSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response (ser.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomerDetail(APIView):
    def get(self, request, pk, format=None):
        cust = Customer.objects.filter(pk=pk)
        ser = CustomerSerializer(cust, many=True)
        return Response(ser.data)

    def put(self, request, pk, format=None):
        cust = Customer.objects.filter(pk=pk).first()
        ser = CustomerSerializer(cust, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response (ser.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        cust = Customer.objects.filter(pk=pk).first()
        cust.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProductList(APIView):
    def get(self, request, format=None):
        prods = Product.objects.all()
        ser = ProductSerializer(prods, many=True)
        return Response (ser.data)

    def post(self, request, format=None):
        ser = ProductSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response (ser.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetail(APIView):
    def get(self, request, pk, format=None):
        prod = Product.objects.filter(pk=pk)
        ser = ProductSerializer(prod, many=True)
        return Response(ser.data)

    def put(self, request, pk, format=None):
        prod = Product.objects.filter(pk=pk).first()
        ser = ProductSerializer(prod, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response (ser.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        prod = Product.objects.filter(pk=pk).first()
        prod.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProductSearch(APIView):
    def post(self, request, search, format=None):
        searchlist = search.split(',', -1)
        res = Product.objects.all()
        for tag in searchlist:
            res = res.filter(tags_unaccent_contains=tag)
        ser = ProductSerializer(res, many=True)
        return Response(ser.data)

class StoreList(APIView):
    def get(self, request, format=None):
        stores = Store.objects.all()
        ser = StoreSerializer(stores, many=True)
        return Response (ser.data)

    def post(self, request, format=None):
        ser = StoreSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response (ser.errors, status=status.HTTP_400_BAD_REQUEST)

class StoreDetail(APIView):
    def get(self, request, pk, format=None):
        store = Store.objects.filter(pk=pk)
        ser = StoreSerializer(store, many=True)
        return Response(ser.data)

    def put(self, request, pk, format=None):
        store = Store.objects.filter(pk=pk).first()
        ser = StoreSerializer(store, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response (ser.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        store = Store.objects.filter(pk=pk).first()
        store.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class LocationInventory(APIView):
    def post(self, request, format=None):
        ser = Has_As_InventorySerializer(request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response (ser.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        inv = Has_As_Inventory.objects.filter(location=request.data["address"], upc=request.data["upc"]).first()
        ser = Has_As_InventorySerializer(inv, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response (ser.errors, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request, format=None):
        query = Has_As_Inventory.objects.filter(location=request.data["address"], upc=request.data["upc"]).first()
        ser = Has_As_InventorySerializer(query)
        return Response(ser.data)

    def delete(self, request, format=None):
        inv = Has_As_Inventory.objects.filter(location=request.data["address"], upc=request.data["upc"]).first()
        inv.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class StockOrd(APIView):
    def post(self, request, format=None):
        neword_id = (Stock_Order.objects.latest('order_id').pk)+1
        ser = Stock_Order(ship_from=request.data["ship_from"], ship_to=request.data["ship_to"], order_id=neword_id)
        if ser.is_valid():
            ser.save()
        else:
            return Response (ser.errors, status=status.HTTP_400_BAD_REQUEST)
        for inc in request.data["includes"]:
            ser2 = Stock_Order_Includes(order_id = neword_id, quantity=request.data["quantity"], upc = request.data["upc"])
            if ser2.is_valid():
                ser2.save()
            else:
                return Response (ser2.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(ser.data, status=status.HTTP_201_CREATED)

class StockOrdDetail(APIView):

    def get(self, request, pk, format=None):
        stk = Stock_Order.objects.filter(pk = pk).first()
        inc = Stock_Order_Includes.objects.filter(order_id = pk)

        ser = Stock_OrderSerializer(stk)
        ser2 = Stock_Order_IncludesSerializer(inc, many=True)

        newdic ={'Includes': ser2.data}
        newdic.update(ser.data)

        return Response(newdic)

class CustomerOrd(APIView):
    def post(self, request, format=None):
        neword_id = (Customer_Order.objects.latest('order_id').pk)+1
        ser = Customer_Order(ordered_at=request.data["ordered_at"], date=request.data["date"], time=request.data["time"], total_price=request.data["price"], order_type=request.data["order_type"] ,order_id=neword_id)
        if ser.is_valid():
            ser.save()
        else:
            return Response (ser.errors, status=status.HTTP_400_BAD_REQUEST)
        for inc in request.data["includes"]:
            ser2 = Ord_Includes(order_id = neword_id, quantity=request.data["quantity"], upc = request.data["upc"])
            if ser2.is_valid():
                ser2.save()
            else:
                return Response (ser2.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(ser.data, status=status.HTTP_201_CREATED)

class CustomerOrdDetail(APIView):

    def get(self, request, pk, format=None):
        stk = Customer_Order.objects.filter(pk = pk).first()
        inc = Ord_Includes.objects.filter(order_id = pk)

        ser = Customer_OrderSerializer(stk)
        ser2 = Ord_IncludesSerializer(inc, many=True)

        newdic ={'Includes': ser2.data}
        newdic.update(ser.data)

        return Response(newdic)
class AccountList(APIView):
    def post(self, request, format=None):
        ser = AccountSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response (ser.errors, status=status.HTTP_400_BAD_REQUEST)

class AccountDetail(APIView):
    def get(self, request, pk, format=None):
        employees = Employee.objects.filter(pk=pk)
        ser = EmployeeSerializer(employees, many=True)
        return Response (ser.data)

    def put(self, request, pk, format=None):
        emp = Account.objects.filter(pk=pk).first()
        ser = AccountSerializer(emp, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response (ser.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        emp = Account.objects.filter(pk=pk)
        emp.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ShipmentList(APIView):

    def post(self, request, format=None):
        ser = Shipment(shipping_co = request.data["ship_co"], tracking_no = request.data["tracking_no"], eta=request.data["eta"], ship_date = request.data["ship_date"], order_id = request.data["order_id"])
        if ser.is_valid():
            ser.save()
        else:
            return Response (ser.errors, status=status.HTTP_400_BAD_REQUEST)
        for inc in request.data["includes"]:
            ser2 = Ship_Includes(order_id = request.data["order_id"], quantity=request.data["quantity"], upc = request.data["upc"])
            if ser2.is_valid():
                ser2.save()
            else:
                return Response (ser2.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(ser.data, status=status.HTTP_201_CREATED)

class ShipmentDetail(APIView):
    def get(self, request, pk, format=None):
        stk = Shipment.objects.filter(pk = pk).first()
        inc = Ship_Includes.objects.filter(order_id = pk)

        ser = ShipmentSerializer(stk)
        ser2 = Ship_IncludesSerializer(inc, many=True)

        newdic ={'Includes': ser2.data}
        newdic.update(ser.data)

        return Response(newdic)

    def delete(self, request, pk, format=None):
        emp = Shipment.objects.filter(pk=pk)
        emp.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ShipbyordID(APIView):
    def get(self, request, pk, format=None):
        inc = Ship_Includes.objects.filter(order_id = pk)
        ser2 = Ship_IncludesSerializer(inc, many=True)
        return Response(ser2.data)

class WarehouseList(APIView):
    def get(self, request, format=None):
        warehouses = Warehouse.objects.all()
        ser = WarehouseSerializer(warehouses, many=True)
        return Response (ser.data)

    def post(self, request, format=None):
        ser = WarehouseSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response (ser.errors, status=status.HTTP_400_BAD_REQUEST)

class WarehouseDetail(APIView):
    def get(self, request, pk, format=None):
        warehouse = Warehouse.objects.filter(pk=pk)
        ser = WarehouseSerializer(warehouse, many=True)
        return Response(ser.data)

    def put(self, request, pk, format=None):
        warehouse = Warehouse.objects.filter(pk=pk).first()
        ser = WarehouseSerializer(warehouse, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response (ser.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        warehouse = Warehouse.objects.filter(pk=pk).first()
        warehouse.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)