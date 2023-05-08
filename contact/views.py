from django.shortcuts import render, redirect, reverse, get_object_or_404
from .forms import ContactForm, UpdateContactForm
from django.contrib import messages
from .models import Contact


# Create your views here.


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your message has been sent successfully!')
            return redirect('home')
    else:
        form = ContactForm()

    context = {'form': form}
    return render(request, 'contact/contact.html', context)


def contact_management(request):
    contact_forms = Contact.objects.all()
    return render(request, 'contact/contact_management.html', {'contact_forms': contact_forms})


def update_contact_form(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)

    if request.method == 'POST':
        form = UpdateContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_management')
    else:
        form = UpdateContactForm(instance=contact)

    context = {'form': form, 'contact': contact}
    return render(request, 'contact/update_contact_form.html', context)


def delete_contact_form(request, form_id):
    contact_form = get_object_or_404(Contact, id=form_id)
    contact_form.delete()
    messages.success(request, "Contact form successfully deleted.")
    return redirect('contact_management')
