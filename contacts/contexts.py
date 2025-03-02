from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from .models import Contacts, Replied


def contacts_inbox(request):

    user = request.user.id
    if user:
        user_inbox = get_object_or_404(User, username=request.user)
        inbox = Contacts.objects.filter(send_to=user_inbox)
        replied = Replied.objects.filter(name=user_inbox)
        reply_message = Contacts.objects.filter(
            new_reply=True, name=user_inbox)

        unread_messages = inbox.filter(read=False).count()

        message_count = len(inbox)

        reply_num = len(reply_message)

        context = {
            'inbox': inbox,
            'message_count': message_count,
            'unread_messages': unread_messages,
            'replied': replied,
            'reply_num': reply_num,
        }
    else:
        inbox = Contacts.objects.all()

        context = {
            'inbox': inbox
        }

    return context
