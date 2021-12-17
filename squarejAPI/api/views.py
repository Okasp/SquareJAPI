from typing import List
from django.db.models import deletion, manager
from django.http import response
from django.shortcuts import render
from rest_framework.serializers import Serializer
import datetime

from api.apps import ApiConfig
from api.models import *
from .serializers import *
from .models import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

import bcrypt
import base64
import json

class EmployeeList(APIView):
    def get(self, request, format=None):
        employees = Employee.objects.all()
        ser = EmployeeSerializer(employees, many=True)
        a = Location(address="999 Rando street SE Calgary AB")
        a.save()
        b = Location(address="998 Rando street SE Calgaru AB")
        b.save()
        st = Store(address=a)
        st.save()
        wa = Warehouse(address=b, capacity = 3000)
        wa.save()

        g = Customer_Order(order_id=1, ordered_at=st, date = datetime.date(2021, 10, 19), time = datetime.time(10,33,45), total_price = 10.99, order_type = "instore")
        g.save()
        c = Customer(phone_number="(403)999-9999", name = "Jane Doe", address = "444 Testing Road SW Calgary AB")
        c.save()
        place = Places(phone_number=c, order_id = g)
        place.save()
        p = Product(price = 1.01, tags = "test, good, bad", upc=1234567890)
        p.save()
        x = Ord_Includes(order_id=g, quantity = 10, upc = p)
        x.save()

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
            return Response(ser.data, status=status.HTTP_200_OK)
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
            return Response(ser.data, status=status.HTTP_200_OK)
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
        ser = CustomerSerializer(cust)
        return Response(ser.data)

    def put(self, request, pk, format=None):
        cust = Customer.objects.filter(pk=pk).first()
        ser = CustomerSerializer(cust, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_200_OK)
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
        prod = Product.objects.filter(pk=pk).first()
        ser = ProductSerializer(prod)
        return Response(ser.data)

    def put(self, request, pk, format=None):
        prod = Product.objects.filter(pk=pk).first()
        ser = ProductSerializer(prod, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_200_OK)
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
        if not (Location.objects.filter(pk=request.data["address"])):
            l = Location(address=request.data["address"])
            l.save()
        ser = StoreSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response (ser.errors, status=status.HTTP_400_BAD_REQUEST)

class StoreDetail(APIView):
    def get(self, request, pk, format=None):
        store = Store.objects.filter(pk=pk).first()
        ser = StoreSerializer(store)
        return Response(ser.data)

    def put(self, request, pk, format=None):
        if not (Location.objects.filter(pk=request.data["address"])):
            l = Location(address=request.data["address"])
            l.save()

        store = Store.objects.filter(pk=pk).first()
        ser = StoreSerializer(store, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_200_OK)
        else:
            return Response (ser.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        store = Store.objects.filter(pk=pk).first()
        store.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class LocationInventory(APIView):
    def post(self, request, format=None):
        ser = Has_As_InventorySerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response (ser.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        inv = Has_As_Inventory.objects.filter(address=request.data["address"], upc=request.data["upc"]).first()
        ser = Has_As_InventorySerializer(inv, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_200_OK)
        else:
            return Response (ser.errors, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request, format=None):
        query = Has_As_Inventory.objects.filter(address=request.data["address"], upc=request.data["upc"]).first()
        ser = Has_As_InventorySerializer(query)
        return Response(ser.data)

    def delete(self, request, format=None):
        inv = Has_As_Inventory.objects.filter(addressn=request.data["address"], upc=request.data["upc"]).first()
        inv.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class StockOrd(APIView):
    def post(self, request, format=None):
        neword_id = 1 #(Stock_Order.objects.latest('order_id').pk)+1
        ser = Stock_Order(ship_from=Warehouse.objects.filter(pk=request.data["ship_from"]).first(), ship_to=Store.objects.filter(pk=request.data["ship_to"]).first(), order_id=neword_id)
        ser.save()

           # return Response (ser.errors, status=status.HTTP_400_BAD_REQUEST)
        for inc in request.data["includes"]:
            ser2 = Stock_Order_Includes(order_id = ser, quantity=inc["quantity"], upc = Product.objects.filter(pk = inc["upc"]).first())
            ser2.save()

                #return Response (ser2.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(Stock_OrderSerializer(ser).data, status=status.HTTP_201_CREATED)

class StockOrdDetail(APIView):

    def get(self, request, pk, format=None):
        stk = Stock_Order.objects.filter(pk = pk).first()
        inc = Stock_Order_Includes.objects.filter(order_id = pk)

        ser = Stock_OrderSerializer(stk)
        ser2 = Stock_Order_IncludesSerializer(inc)

        newdic ={'Includes': ser2.data}
        newdic.update(ser.data)

        return Response(newdic)
    
    def delete(self, request, pk, format=None):
        stk = Stock_Order.objects.filter(pk=pk)
        stk.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class CustomerOrd(APIView):
    def post(self, request, format=None):
        neword_id = (Customer_Order.objects.latest('order_id').pk)+1
        #try:
        ser = Customer_Order(ordered_at=request.data["ordered_at"], date=request.data["date"], time=request.data["time"], total_price=request.data["total_price"], order_type=request.data["order_type"] ,order_id=neword_id)
        ser.save()
        ser3 = Places(order_id = ser, phone_number=Customer.objects.filter(pk = request.data["ordered_by"]).first())
        ser3.save()
        #except:
            #return Response (status=status.HTTP_400_BAD_REQUEST)
        for inc in request.data["includes"]:
            try:
                ser2 = Ord_Includes(order_id = ser, quantity=inc["quantity"], upc = Product.objects.filter(pk=inc["upc"]).first())
                ser2.save()
            except:
                return Response (ser2.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(Customer_OrderSerializer(ser).data, status=status.HTTP_201_CREATED)

class CustomerOrdDetail(APIView):

    def get(self, request, pk, format=None):
        stk = Customer_Order.objects.filter(pk = pk).first()
        inc = Ord_Includes.objects.filter(order_id = pk)

        ser = Customer_OrderSerializer(stk)
        ser2 = Ord_IncludesSerializer(inc, many=True)

        newdic ={'includes': ser2.data}
        newdic.update(ser.data)

        return Response(newdic)

    def delete(self, request, pk, format=None):
        ord = Customer_Order.objects.filter(pk=pk)
        ord.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

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
        employees = Account.objects.filter(pk=pk).first()
        ser = AccountSerializer(employees, many=True)
        return Response (ser.data)

    def put(self, request, pk, format=None):
        emp = Account.objects.filter(pk=pk).first()
        ser = AccountSerializer(emp, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_200_OK)
        else:
            return Response (ser.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        emp = Account.objects.filter(pk=pk)
        emp.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ShipmentList(APIView):

    def post(self, request, format=None):
        neword_id = Customer_Order.objects.filter(pk = request.data["order_id"]).first()
        ser = Shipment(shipping_co = request.data["shipping_co"], tracking_no = request.data["tracking_no"], eta=request.data["eta"], ship_date = request.data["ship_date"], order_id = neword_id)
        ser.save()

            #return Response (ser.errors, status=status.HTTP_400_BAD_REQUEST)
        for inc in request.data["includes"]:
            ser2 = Ship_Includes(tracking_no = ser, quantity=inc["quantity"], upc = Product.objects.filter(pk = inc["upc"]).first())
            ser2.save()

                #return Response (ser2.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(ShipmentSerializer(ser).data, status=status.HTTP_201_CREATED)

class ShipmentDetail(APIView):
    def get(self, request, pk, format=None):
        stk = Shipment.objects.filter(pk = pk).first()
        inc = Ship_Includes.objects.filter(tracking_no = pk)

        ser = ShipmentSerializer(stk)
        ser2 = Ship_IncludesSerializer(inc, many=True)

        newdic ={'includes': ser2.data}
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
        if not (Location.objects.filter(pk=request.data["address"])):
            l = Location(address=request.data["address"])
            l.save()
        ser = WarehouseSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response (ser.errors, status=status.HTTP_400_BAD_REQUEST)

class WarehouseDetail(APIView):
    def get(self, request, pk, format=None):
        warehouse = Warehouse.objects.filter(pk=pk).first()
        ser = WarehouseSerializer(warehouse)
        return Response(ser.data)

    def put(self, request, pk, format=None):
        if not (Location.objects.filter(pk=request.data["address"])):
            l = Location(address=request.data["address"])
            l.save()
        warehouse = Warehouse.objects.filter(pk=pk).first()
        ser = WarehouseSerializer(warehouse, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_200_OK)
        else:
            return Response (ser.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        warehouse = Warehouse.objects.filter(pk=pk).first()
        warehouse.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AccountList(APIView):
    def get(self, request, format=None):
        accounts = Account.objects.all()
        ser = AccountSerializer(accounts, many=True)
        return Response (ser.data)

    def post(self, request, format=None):
        if request.data["acctype"]=="customer":
            emp_id = None
            e_id = None
            if not Customer.objects.filter(pk = request.data["phone_number"]).exists():
                pn = Customer(phone_number = request.data["phone_number"], name = request.data["name"], address = request.data["address"])
                pn.save()
            else:
                pn = Customer.objects.filter(pk = request.data["phone_number"]).first()
        elif request.data["acctype"]=="employee":
            pn = None
            e_id = request.data["employee_id"]
            if not Employee.objects.filter(pk = request.data["employee_id"]).exists():
                newemp_id = (Employee.objects.latest('employee_id').pk)+1
                emp_id = Employee(employee_id = newemp_id, sin = request.data["sin"], address = request.data["address"])
                emp_id.save()
            else:
                emp_id = Employee.objects.filter(pk = request.data["employee_id"]).first()
        else:
            return Response (status=status.HTTP_400_BAD_REQUEST)
        acc = Account(username = request.data["username"],
            name = request.data["name"],
            phone_number = request.data["phone_number"],
            address = request.data["address"],
            salted_pwd_hash = bcrypt.hashpw(bytes(request.data["password"], 'utf-8'), bcrypt.gensalt()),
            acctype = request.data["acctype"],
            email = request.data["email"],
            employee_id = e_id)
        acc.save()

        #CANNOT GET THIS TO WORK WITHOUT FORIEGN KEY VIOLATIONS
        #if pn!= None:
            #Belongs_to.objects.raw("INSERT INTO api_belongs_to (username_id, employee_id_id, phone_number_id) VALUES ('" + acc.username + "', 'null', '" + pn.phone_number + "');")
        #bel = Belongs_to2(pk = Account.objects.filter(pk = acc.username).first(), phone_number = pn)
        #bel.save()
        return Response({"username":acc.username, "email":acc.email}, status=status.HTTP_201_CREATED)
        #else:
            #return Response (ser.errors, status=status.HTTP_400_BAD_REQUEST)

class AccountDetail(APIView):
    def get(self, pk, request, format=None):
        acc = Account.objects.filter(pk=pk).first()
        ser = AccountSerializer(acc)
        return Response(ser.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        acc = Account.objects.filter(pk=pk).first()
        ser = AccountSerializer(acc, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_200_OK)
        else:
            return Response (ser.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        emp = Account.objects.filter(pk=pk)
        emp.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Auth(APIView):

    def post(self, request, format=None):
        acc = Account.objects.filter(pk=request.data["username"]).first()
        if acc==None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if bcrypt.checkpw(bytes(request.data["password"], 'utf-8'), acc.salted_pwd_hash):
            return Response({'acctype': acc.acctype, 'username': acc.username},status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

