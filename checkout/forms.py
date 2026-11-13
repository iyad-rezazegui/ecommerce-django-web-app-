from django import forms
from checkout.models import order

class CheckoutForm(forms.Form):
    full_name = forms.CharField(min_length=5,max_length=15,help_text='اكتب اسمك')
    phone = forms.IntegerField()
    adress = forms.CharField(max_length=100)
    class Meta :
        model=order
        fields=['full_name','phone','adress']


              
  
   