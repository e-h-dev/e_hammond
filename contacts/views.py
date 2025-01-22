from django.shortcuts import render, reverse, redirect, get_object_or_404
from .models import Contacts
from .forms import ContactForm

# Create your views here.

def contacts(request):


    # inbox = Contacts.objects.all()

    # context = {
    #     'inbox': inbox,
    # }

    return render(request, 'contacts/contacts.html')




def open_message(request, contact_id):
    """ A view to show individual products and details """

    inbox = Contacts.objects.get(id=contact_id)
    inbox.read = True
    inbox.save()


    template = 'contacts/open_message.html'


    context = {
        'inbox': inbox
    }

    return render(request, template, context)



def compose_message(request):
    """
    A view to send a message
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('contacts'))
        else:
            print(form.errors.as_data())



    else:
        form = ContactForm()

    template = 'contacts/compose_message.html'
    context = {
        'form': form,
    }

    return render(request, template)


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


