import random
import string
from store.models import product
class Basket():
    def __init__(self, request):      #we do the request we check the request if the user has a session or not and we create one if he doesn't have one
        self.session=request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket=self.session['skey']={}# we create a session for the user and we store the basket in it
        self.basket = basket
       
    def add_basket(self, product, productqty):
        # 1. Convert to string immediately!
        product_id = str(product.id) 
        qty = int(productqty)
        
        if product_id not in self.basket:
            self.basket[product_id] = {'price': (product.price), 'qty': qty}
        else:
            # 2. Use the string 'qty', not the variable qty!
            # You can also use += if you want to add to the existing amount
            self.basket[product_id]['qty'] = int(qty) 
        self.save()
    
    def delete(self, product):
            """
            Delete item from session data
            """
            product_id=str(product)
            if product_id in self.basket:
                del self.basket[product_id]
            self.save()
    def update(self, product, productqty):
        """
        Update values in session data
        """
        product_id = str(product)
        proqty=int(productqty)
        if product_id in self.basket:
            self.basket[product_id]['qty'] = proqty
        self.save()
    def __iter__(self):
        """
        Collect the product_id in the session data to query the database
        and return products
        """
        product_ids = self.basket.keys()
        
        # FIX: Changed .products.filter() to .objects.filter()
        products = product.objects.filter(id__in=product_ids)
        
        basket = self.basket.copy()

        # Changed variable to 'prod' to avoid any confusion with the Model name
        for prod in products:
            basket[str(prod.id)]['product'] = prod

        for item in basket.values():
            item['price'] = float(item['price'])
            item['total_price'] = item['price'] * item['qty']
            item['product_name']=item['product'].name
            yield item
 
    def __len__(self):
        """
        Get the basket data and count the qty of items
        """
        return sum(item['qty'] for item in self.basket.values())
    def get_total_price(self):
        return sum((item['price'])*(item['qty']) for item in self.basket.values())

    def save(self):
        self.session.modified = True