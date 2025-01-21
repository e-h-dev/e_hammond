from .models import Contacts


def contacts_inbox(request):

    inbox = Contacts.objects.all()

    context = {
        'inbox': inbox,
    }

    return context