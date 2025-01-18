from django.shortcuts import render
from .models import Contacts

# Create your views here.

def contacts(request):

    inbox = Contacts.objects.all()

    context = {
        'inbox' : inbox
    }

    return render(request, 'contacts/contacts.html', context)
