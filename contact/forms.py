from .models import Contact, Comment
from django import forms


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']


class UpdateContactForm(forms.ModelForm):
    status = forms.ChoiceField(
        choices=Contact.STATUS_CHOICES, widget=forms.Select)

    class Meta:
        model = Contact
        fields = ['name', 'email', 'message', 'status']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
