<<<<<<< HEAD
from django import forms


class AddToCheckout(forms.Form):
    quantity = forms.IntegerField(min_value=1)
    product_id = forms.CharField(max_length=100)
    command = forms.CharField(max_length=100)
=======
from django import forms


class AddToCheckout(forms.Form):
    quantity = forms.IntegerField(min_value=1)
    product_id = forms.CharField(max_length=100)
    command = forms.CharField(max_length=100)
>>>>>>> 970411dd3de5ed996f005820fcc60d8b4bc41da5
    