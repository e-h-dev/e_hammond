from .models import Contacts


def contacts_inbox(request):

    inbox = Contacts.objects.all()

    message_count = (len(inbox))

    context = {
        'inbox': inbox,
        'message_count': message_count
    }

    return context