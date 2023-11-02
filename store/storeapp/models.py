from django.db import models
from django.contrib.auth.models import User
from productapp.models import Product
# Create your models here.
class Cart(models.Model): # the order we want comes to cart
    uid=models.ForeignKey(User,on_delete=models.CASCADE,db_column='uid')
    pid=models.ForeignKey(Product,on_delete=models.CASCADE,db_column='pid')
    qty=models.IntegerField(default=1)

class Order(models.Model): # then when we place order then we trasnfer products from cart to order, then the cart table is cleared
    order_id = models.CharField(max_length=50)
    uid=models.ForeignKey(User,on_delete=models.CASCADE,db_column='uid')
    pid=models.ForeignKey(Product,on_delete=models.CASCADE,db_column='pid')
    qty=models.IntegerField(default=1)
    is_completed = models.BooleanField(default=False)
