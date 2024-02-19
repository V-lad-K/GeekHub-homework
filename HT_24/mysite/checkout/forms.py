from django import forms


class AddToCheckout(forms.Form):
    quantity = forms.IntegerField(min_value=1)
    product_id = forms.CharField(max_length=100)
    command = forms.CharField(max_length=100)
    