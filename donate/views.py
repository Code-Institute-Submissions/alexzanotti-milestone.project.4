from django.shortcuts import render

# Create your views here.


def donate(request):
    """ A view to render the donate page """

    return render(request, 'home/donate.html')