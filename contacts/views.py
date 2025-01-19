from django.shortcuts import render, reverse, get_object_or_404
from .models import Contacts
from .forms import ContactForm

# Create your views here.

def contacts(request):

    inbox = Contacts.objects.all()

    context = {
        'inbox': inbox
    }

    return render(request, 'contacts/contacts.html', context)




def open_message(request, contact_id):
    """ A view to show individual products and details """

    inbox = get_object_or_404(Contacts, pk=contact_id)

    template = 'contacts/open_message.html'

    #return render(reverse, template, ('contacts'))


    context = {
        'inbox': inbox
    }

    return render(request, template, context)


# def edit_contact(request, contact_id):


#     contact = get_object_or_404(Contacts, pk=contact_id)

#     if request.method == 'POST':
#         form = ContactForm(request.POST, request.FILES, instance=contact)
#         if form.is_valid():
#             form.save()
#             return redirect('contacts')
        
#     else:

#         form = ContactForm(instance=contact)
    
#     template = 'contacts/contacts.html'
#     context = {
#         'form': form,
#         'contact': contact,
#     }

#     return render(request, template, context)


