from django.db import models
from django.shortcuts import redirect, HttpResponseRedirect


# Create your models here.
class Category(models.Model):
    cname = models.CharField(max_length=50, null=False)
    cimage = models.ImageField(upload_to='images/categoryImages', null=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cname
    
    
    class Meta:
        verbose_name = 'category'
        db_table = 'category'

        permissions = [
            ("category_check_permission", " check category permission s valid or not"),
        ]


class Product(models.Model):
    name = models.CharField(max_length=50, null=False)
    price = models.IntegerField(null=False)
    pdesc = models.TextField(max_length=150, null=False)
    image = models.ImageField(upload_to='images/productImages', null=False)
    pcat = models.ForeignKey(Category, null=False, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'products'
        db_table = 'products'


class Order(models.Model):
    statusChoices = (
        ('p', 'pending'),
        ('c', 'completed')
    )

    productid = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False)
    status = models.CharField(choices=statusChoices, max_length=50, null=False)
    amount = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.oname
    
    class Meta:
        verbose_name = 'order'
        db_table = 'order'

        



