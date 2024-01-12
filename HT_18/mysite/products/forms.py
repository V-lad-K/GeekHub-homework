from django import forms
from .models import ScrapingTask


class AddScrapingTaskForm(forms.ModelForm):
    class Meta:
        model = ScrapingTask
        fields = "__all__"

# class AddProductForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = "__all__"
