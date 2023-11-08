from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.IntegerField()
    address = models.CharField(max_length=254)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Customer - {self.name}'

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    product_quantity = models.IntegerField()
    product_acceptance_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Product - {self.product_name}'

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    price_total_order = models.DecimalField(max_digits=8, decimal_places=2)
    date_order = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Customer - {self.customer},\nProducts - {self.products},\nTotal = {self.price_total_order},\ndate order - {self.date_order}'

class ProductImg(models.Model):
    product_name = models.CharField(max_length=100)
    product_description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    product_quantity = models.IntegerField()
    product_acceptance_date = models.DateTimeField(auto_now_add=True)
    product_img = models.ImageField(upload_to='imges_product/')

class MetaProductImg(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='img_prod/')
