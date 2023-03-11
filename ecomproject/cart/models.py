from django.db import models

from ecomapp.models import Product


# Create your models here.
class Cart(models.Model):
    cartid=models.CharField(max_length=250,blank=True)
    datead=models.DateField(auto_now_add=True)
    class Meta:
        db_table='Cart'
        ordering=['datead']
    def __str__(self):
        return "{}".format(self.cartid)
class Cartitem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    active=models.BooleanField(default=True)

    class Meta:
        db_table='Cartitem'

    def Total(self):
        return self.product.price * self.quantity
    def __str__(self):
        return "{}".format(self.product)