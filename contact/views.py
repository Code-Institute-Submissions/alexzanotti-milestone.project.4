from django.shortcuts import render, redirect, reverse, get_object_or_404
from .forms import ContactForm, UpdateContactForm, CommentForm
from django.contrib import messages
from .models import Contact, Comment


# Create your views here.


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your message has been sent successfully!')
            return redirect('contact_success')
    else:
        form = ContactForm()

    context = {'form': form}
    return render(request, 'contact/contact.html', context)



def contact_management(request):
    contact_forms = Contact.objects.all()
    return render(request, 'contact/contact_management.html', {'contact_forms': contact_forms})


def update_contact_form(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    comments = Comment.objects.filter(contact=contact)

    if request.method == 'POST':
        form = UpdateContactForm(request.POST, instance=contact)
        comment_form = CommentForm(request.POST)

        if form.is_valid():
            form.save()

        if comment_form.is_valid() and request.user.is_superuser:
            comment = comment_form.save(commit=False)
            comment.contact = contact
            comment.author = request.user
            comment.save()

        return redirect('update_contact_form', contact_id=contact.id)
    else:
        form = UpdateContactForm(instance=contact)
        comment_form = CommentForm()

    context = {'form': form, 'comment_form': comment_form,
               'contact': contact, 'comments': comments}
    return render(request, 'contact/update_contact_form.html', context)


def delete_contact_form(request, form_id):
    contact_form = get_object_or_404(Contact, id=form_id)
    contact_form.delete()
    messages.success(request, "Contact form successfully deleted.")
    return redirect('contact_management')

def contact_success(request):
    return render(request, 'contact/contact_success.html')