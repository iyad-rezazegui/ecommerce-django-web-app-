from django.contrib import admin

from store.models import Categories , product , order


# Register your models here.
@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields={'slug':('name',)}

@admin.register(product) 
class productAdmin(admin.ModelAdmin):
    list_display=['name','slug','serial_number','is_created','is_updated','price','description','is_in_stock','quantity']
    list_filter=['is_in_stock','is_created','is_updated','quantity']
    list_editable=['is_in_stock','price','quantity']
    prepopulated_fields={'slug':('name',)}

@admin.register(order)
class orderAdmin(admin.ModelAdmin):
    list_display=['customer_name','customer_phone','customer_wilaya','product','quantity','is_created']
    list_filter=['status','is_created']
