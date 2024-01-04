from django import forms
from .models import ScrapingTask
from .models import Product


class AddScrapingTaskForm(forms.ModelForm):
    class Meta:
        model = ScrapingTask
        fields = "__all__"


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
