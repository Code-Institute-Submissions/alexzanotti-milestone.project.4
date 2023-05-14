from django import forms
from .models import Category, Plan, Comment


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']


class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ['name', 'category', 'description',
                  'price', 'image_field']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
