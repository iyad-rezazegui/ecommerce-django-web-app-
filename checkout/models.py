from django.db import models

# Create your models here.
class order(models.Model):
    full_name=models.CharField(max_length=20)
    phone=models.IntegerField()
    adress=models.CharField(max_length=20)
    products=models.TextField(default='hi')
    price = models.IntegerField(default=0)
    date=models.DateTimeField(auto_now_add=True,null=True)

