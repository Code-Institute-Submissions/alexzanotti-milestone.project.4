from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('user_name', 'email', 'phone_number',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'user_name': 'User Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
        }

        self.fields['user_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
