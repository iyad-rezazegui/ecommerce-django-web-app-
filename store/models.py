from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Categories(models.Model):
    name = models.CharField(max_length=255,db_index=True)
    slug = models.SlugField(max_length=255,unique=True)
    class meta :
        verbose_name_plural='categories'  # why did he do it anyways 
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('store:category_products', args=[self.slug])
    
    
class product(models.Model):
    
    name=models.CharField(max_length=255,db_index=True,null=True)
    slug=models.SlugField(max_length=255,unique=True,null=True)
    category=models.ForeignKey(Categories,on_delete=models.CASCADE,null=True,name='product_category')
    serial_number=models.IntegerField(null=True) # i need to search for it next time and we might have / and * 
    is_created=models.DateTimeField(auto_now_add=True,null=True)
    is_updated=models.DateTimeField(auto_now=True,null=True)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    description=models.TextField(null=True)
    image=models.ImageField(upload_to='images/',null=True)
    price=models.IntegerField(null=True)
    is_in_stock=models.BooleanField(default=True,null=True)
    quantity=models.IntegerField(null=True)
    class Meta:
        verbose_name_plural='products'
        ordering=('-is_created',) # takes the same name as the veriable
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.slug])
    

class order(models.Model):
    order_number=models.IntegerField(null=True)
    product=models.ForeignKey(product,on_delete=models.CASCADE,null=True)
    quantity=models.IntegerField(null=True)
    is_created=models.DateTimeField(auto_now_add=True,null=True)
    is_updated=models.DateTimeField(auto_now=True,null=True)
    Status=(('Pending','Pending'),('Approved','Approved'),('Rejected','Rejected'),('delevred','delevred'),('requested','not_requested'))
    customer_name=models.CharField(max_length=255,db_index=True,default='non')
    customer_phone=models.CharField(max_length=255,db_index=True)
    customer_wilaya=models.CharField(max_length=255,db_index=True)
    status=models.CharField(max_length=255,choices=Status,default='not_requested',null=True)
    class Meta:
        verbose_name_plural='orders'
        ordering=('-is_created',)
    def __str__(self):
        return self.order_number



