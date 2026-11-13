from django.shortcuts import render
from basket.basket import Basket
from checkout.forms import CheckoutForm
from checkout.models import order 
from django.http import HttpResponse


def order_placed(request):
    basket = Basket(request)
    return render(request, 'store/checkout/orderplaced.html', {'basket': basket})

def paid(request):
    if request.method == 'POST':
        basket=Basket(request)
        form=CheckoutForm(request.POST )
        if form.is_valid():
            phonee=form.cleaned_data['phone']
            name=form.cleaned_data['full_name']
            adresss=form.cleaned_data['adress']
            text =''
            pricee = 0
            for key in basket:
                text = text + key['product_name']+'     '
                pricee = pricee + key['total_price']
            order.objects.create(full_name=name,phone=phonee,adress=adresss,products=text,price=pricee)
            return HttpResponse('congrats will ship it as quick as possible ')
        return render(request ,'store/checkout/orderplaced.html',{'form':form} )




