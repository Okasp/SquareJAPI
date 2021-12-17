from django.db import models

# Create your models here.
class Account(models.Model):
    username = models.CharField(max_length=32, primary_key=True)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    salted_pwd_hash = models.CharField(max_length=256)
    salt = models.IntegerField()
    acctype = models.CharField(max_length=20)
    email = models.EmailField()

class Employee(models.Model):
    employee_id = models.IntegerField(primary_key=True)
    sin = models.IntegerField()
    address = models.CharField(max_length=100)

class Customer(models.Model):
    phone_number = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)

class Location(models.Model):
    address = models.CharField(max_length=100, primary_key=True)

class Store(models.Model):
    address = models.OneToOneField(Location, on_delete=models.CASCADE, primary_key=True)

class Customer_Order(models.Model):
    order_id = models.IntegerField(primary_key=True)
    ordered_at = models.ForeignKey(Store, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField()
    time = models.TimeField()
    total_price = models.FloatField()
    order_type = models.CharField(max_length=10)

class Places(models.Model):
    order_id = models.OneToOneField(Customer_Order, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.ForeignKey(Customer, on_delete=models.CASCADE)

class Product(models.Model):
    price = models.FloatField()
    tags = models.CharField(max_length=1000)
    upc = models.IntegerField(primary_key=True)

class Ord_Includes(models.Model):
    order_id = models.ForeignKey(Customer_Order, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    upc = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    class Meta:
        unique_together = ['order_id', 'upc']

class Belongs_to(models.Model):
    username = models.OneToOneField(Account, primary_key=True, on_delete=models.CASCADE)
    employee_id = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.CASCADE)
    phone_number = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.CASCADE)

class Manager(models.Model):
    employee_id = models.IntegerField(primary_key=True)
    sin = models.IntegerField()
    address = models.CharField(max_length=100)

class Warehouse(models.Model):
    address = models.OneToOneField(Location, on_delete=models.CASCADE, primary_key=True)
    capacity = models.IntegerField()

class Has_As_Inventory(models.Model):
    address = models.ForeignKey(Location, on_delete=models.CASCADE)
    upc = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        unique_together = ['address', 'upc']

class Completes(models.Model):
    order_id = models.OneToOneField(Customer_Order, on_delete=models.CASCADE, primary_key=True)
    employee_id = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)

class Assigned_To(models.Model):
    order_id = models.OneToOneField(Customer_Order, on_delete=models.CASCADE, primary_key=True)
    employee_id = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)

class Shipment(models.Model):
    shipping_co = models.CharField(max_length=50)
    tracking_no = models.CharField(max_length=50, primary_key=True)
    eta = models.DateField()
    ship_date = models.DateField()
    order_id = models.ForeignKey(Customer_Order, on_delete=models.CASCADE)

class Ship_Includes(models.Model):
   quantity = models.IntegerField()
   upc = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True) 
   tracking_no = models.ForeignKey(Shipment, on_delete=models.CASCADE)

class Responsible_For(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    order_id = models.OneToOneField(Customer_Order, on_delete=models.CASCADE, primary_key=True)

class Stock_Order(models.Model):
    order_id = models.IntegerField(primary_key=True)
    ship_from = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    ship_to = models.ForeignKey(Store, on_delete=models.CASCADE)

class Stock_Order_Includes(models.Model):
    order_id = models.ForeignKey(Stock_Order, on_delete=models.CASCADE)
    upc = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()