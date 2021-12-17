from rest_framework import serializers
from api.models import *

class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = 'username, name, acctype, address, phone_number, email'

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = '__all__'

class StoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Store
        fields = '__all__'

class Customer_OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer_Order
        fields = '__all__'

class PlacesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Places
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

class Ord_IncludesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ord_Includes
        fields = '__all__'

class Belongs_toSerializer(serializers.ModelSerializer):

    class Meta:
        model = Belongs_to
        fields = '__all__'

class ManagerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manager
        fields = '__all__'

class WarehouseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Warehouse
        fields = '__all__'

class Has_As_InventorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Has_As_Inventory
        fields = '__all__'

class CompletesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Completes
        fields = '__all__'

class Assigned_ToSerializer(serializers.ModelSerializer):

    class Meta:
        model = Assigned_To
        fields = '__all__'
class ShipmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shipment
        fields = '__all__'

class Ship_IncludesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ship_Includes
        fields = '__all__'

class Responsible_ForSerializer(serializers.ModelSerializer):

    class Meta:
        model = Responsible_For
        fields = '__all__'

class Stock_OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stock_Order
        fields = '__all__'

class Stock_Order_IncludesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stock_Order_Includes
        fields = '__all__'