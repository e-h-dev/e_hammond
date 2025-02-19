from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from .models import Contacts, Replied


def contacts_inbox(request):

    user = request.user.id
    if user:
        user_inbox = get_object_or_404(User, username=request.user)
        inbox = Contacts.objects.filter(send_to=user_inbox)
        replied = Replied.objects.filter(name=user_inbox)

        replied_count = len(replied)

        inbox_replied_count = replied_count + 1

        unread_messages = inbox.filter(read=False).count()

        message_count = len(inbox)

        context = {
            'inbox': inbox,
            'message_count': message_count,
            'unread_messages': unread_messages,
            'replied': replied,
            'replied_count': replied_count,
            'inbox_replied_count': inbox_replied_count
        }
    else:
        inbox = Contacts.objects.all()

        context = {
            'inbox': inbox
        }

    return context
