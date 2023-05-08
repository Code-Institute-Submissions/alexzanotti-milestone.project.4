from django import forms
from .models import Contact


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
