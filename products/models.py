from django.db import models
from smart_selects.db_fields import (
    ChainedForeignKey,
    ChainedManyToManyField,
    GroupedForeignKey,
    )


# Create your models here.
# Products have Supplier > categories >brands> Sub_Brand and the products tables

class Supplier (models.Model):
    Supplier_Id = models.AutoField(primary_key=True)
    Supplier_Name = models.CharField(max_length=30, blank=False, null=False)

    def __str__(self):
        return self.Supplier_Name

class Category (models.Model):
    Category_Id = models.AutoField(primary_key=True)
    Category_Name = models.CharField(max_length=20, blank=False, null=False)
    Supplier = models.ForeignKey (Supplier, on_delete=models.PROTECT, related_name='categories')

    def __str__(self):
        return self.Category_Name
    
class Brand (models.Model):
    Brand_Id = models.AutoField(primary_key=True)
    Brand_Name = models.CharField(max_length=20, blank=False, null=False)
    Category = models.ForeignKey (Category, on_delete=models.PROTECT, related_name='brands')

    def __str__(self):
        return self.Brand
    
class Sub_Brand (models.Model):
    Sub_Brand_Id = models.AutoField(primary_key=True)
    Sub_Brand_Name = models.CharField(max_length=20, blank=False, null=False)
    Brand = models.ForeignKey (Brand, on_delete=models.PROTECT, related_name='sub_brands')

    def __str__(self):
        return self.Sub_Brand

class Products (models.Model):
    Product_Id = models.AutoField(primary_key=True)
    Product_Code = models.CharField(max_length=10,unique=True,null=False)
    Product_description = models.CharField(max_length=50, blank=False, null=False)
    Sub_Brand = models.ForeignKey (Sub_Brand, on_delete=models.PROTECT, related_name='products')
    Lowest_Selling_Units = models.PositiveIntegerField(blank=False, null=False)
    Highest_Selling_Units = models.PositiveIntegerField(blank=False, null=False)
    Supplier_Selling_Units = models.PositiveIntegerField(blank=False, null=False)

    def __str__(self):
        return self.Product_description