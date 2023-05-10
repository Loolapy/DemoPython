from django.db import models
from Kite.models import Product
# Create your models here.

class Cart(models.Model):
    cart_id=models.CharField(max_length=200, blank=True)
    date_add=models.DateField(auto_now_add=True)

    class Meta:
        db_table='Cart'
        ordering=['date_add']
    def __str__(self):
        return '{}'.format(self.cart_id)

class Cartitem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    Qty=models.IntegerField()
    active=models.BooleanField(default=True)

    class Meta:
        db_table='Cartitem'
    def Sub_total(self):
        return self.product.price * self.Qty
    def __str__(self):
        return '{}'.format(self.product)
