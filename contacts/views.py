from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Contacts, Replied
from .forms import ContactForm, ReplyForm
from .admin import ContactAdmin

# Create your views here.


@login_required
def contacts(request):

    inbox = Contacts.objects.all().order_by('-date', '-time')

    context = {
        'inbox': inbox,
    }

    return render(request, 'contacts/contacts.html', context)


@login_required
def sent_messages(request):

    inbox = Contacts.objects.all().order_by('-date', '-time')

    context = {
        'inbox': inbox,
    }

    return render(request, 'contacts/sent_messages.html', context)



@login_required
def open_message(request, contact_id):
    """ A view open and display contact message """

    inbox = Contacts.objects.get(id=contact_id)
    inbox.read = True
    inbox.save()

    template = 'contacts/open_message.html'

    context = {
        'inbox': inbox
    }

    return render(request, template, context)



def mark_unread(request, contact_id):
    
    inbox = Contacts.objects.get(id=contact_id)
    inbox.read = False
    inbox.save()

    return redirect(reverse('contacts'))



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




# def reply_message(request, contact_id):
#     """
#     A view to reply to a message
#     """
#     inbox = Contacts.objects.get(id=contact_id)

#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse('contacts'))
#         else:
#             print(form.errors.as_data())

#     else:
#         form = ContactForm()

#     template = 'contacts/reply_message.html'
#     context = {
#         'form': form,
#         'inbox': inbox,
#     }

#     return render(request, template, context)


def reply_message(request, contact_id):
    """
    A view to reply to a message
    """
    inbox = Contacts.objects.get(id=contact_id)

    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('contacts'))
        else:
            print(form.errors.as_data())

    else:
        form = ReplyForm()

    template = 'contacts/reply_message.html'
    context = {
        'form': form,
        'inbox': inbox,
    }

    return render(request, template, context)



def delete_message(request, contact_id):
    """ A view to delete contacts """

    inbox = Contacts.objects.get(id=contact_id)
    inbox.delete()

    return redirect(reverse('contacts'))