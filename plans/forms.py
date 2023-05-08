from django import forms
from .models import Category, Plan

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']


class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ['name', 'category', 'description',
                  'price', 'image_urlfield', 'image_field']
