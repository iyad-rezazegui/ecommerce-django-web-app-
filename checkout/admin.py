from django.contrib import admin
from checkout.models import order

# Register your models here.
@admin.register(order)
class orderAdmin(admin.ModelAdmin):
    list_display=['full_name','phone','adress','date']