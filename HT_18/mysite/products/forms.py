from django import forms
from .models import ScrapingTask


class AddScrapingTaskForm(forms.ModelForm):
    class Meta:
        model = ScrapingTask
        fields = "__all__"
