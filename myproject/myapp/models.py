from django.db import models


# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=25)
    reg_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.email}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    quantity = models.IntegerField(default=0)
    add_date = models.DateTimeField(auto_now_add=True)


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_DEFAULT, default='ex_client')
    products = models.ManyToManyField(Product, through='Enrollment')
    date_ordered = models.DateTimeField(auto_now_add=True)
    total_order = models.DecimalField(max_digits=9, decimal_places=2)


class Enrollment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

