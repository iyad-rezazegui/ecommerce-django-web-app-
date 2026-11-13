from django.shortcuts import render
from basket.basket import Basket
from django.http import JsonResponse
from store.models import product
from django.shortcuts import get_object_or_404

def basket_summary(request):
    basket = Basket(request)
    return render(request, 'store/basket/summary.html', {'basket': basket})

def basket_add(request):
    basket = Basket(request) # were grabing the session data    
    if request.POST.get('action') == 'post':  
        product_id = str(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        Product = get_object_or_404(product, id=product_id)
        basket.add_basket(product=Product, productqty=product_qty)
        basketqty = len(basket)
        response = JsonResponse({'qty': basketqty})
        return response


def basket_delete(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = str(request.POST.get('productid'))
        basket.delete(product=product_id)
        basketqty = basket.__len__()
        baskettotal = basket.get_total_price()
        response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal})
        return response
def basket_update(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = str(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        basket.update(product=product_id, productqty=product_qty)
        basketqty = basket.__len__()
        baskettotal = basket.get_total_price()
        response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal})
        return response
    