from django.shortcuts import get_object_or_404, render
from .models import Categories, product

# Create your views here.
# request for the user to get the data from the database and send it to the template
def categories(request):
    return {
        'categories': Categories.objects.all()
    }
def all_products(request):
    products = product.objects.all() # this is an sql querry that would get every product from the database and store it in the variable products
    return render(request, 'store/home.html', {'products': products}) # laod the template and send the data to it
    
def product_detail(request, slug):
    Product = get_object_or_404(product, slug=slug, is_in_stock=True)
    return render(request, 'store/products/detail.html', {'product': Product})

def category_products(request, slug):
    category = get_object_or_404(Categories, slug=slug)
    products = product.objects.filter(product_category=category, is_in_stock=True)
    return render(request, 'store/products/category.html', {'products': products, 'category': category})
