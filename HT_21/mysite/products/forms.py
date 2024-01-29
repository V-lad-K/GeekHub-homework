from django import forms

from .models import ScrapingTask
from .models import Product


class AddScrapingTaskForm(forms.ModelForm):
    class Meta:
        model = ScrapingTask
        fields = "__all__"


class EditProductForm(forms.ModelForm):
    command = forms.CharField(max_length=50, widget=forms.HiddenInput())

    class Meta:
        model = Product
        fields = [
            "name", "price", "short_description", "brand_name",
            "category_id", "product_link"
        ]


class AddToCheckout(forms.Form):
    quantity = forms.IntegerField(min_value=1)
    product_id = forms.CharField(max_length=100)
    command = forms.CharField(max_length=100)