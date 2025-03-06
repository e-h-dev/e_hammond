from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from .models import Contacts, Replied


def contacts_inbox(request):

    user = request.user.id
    if user:
        user_inbox = get_object_or_404(User, username=request.user)
        inbox = Contacts.objects.filter(send_to=user_inbox)
        sent_messages = Contacts.objects.filter(name=user_inbox)
        displayed_reply = Contacts.objects.filter(
            has_reply=True, name=user_inbox)
        replied = Replied.objects.filter(name=user_inbox)
        reply_message = Contacts.objects.filter(
             new_reply=True, send_to=user_inbox)
        reply_inbox_message = Contacts.objects.filter(
             new_reply=True, name=user_inbox)

        unread_recieved_messages = inbox.filter(read=False).count()
        unread_sent_messages = sent_messages.filter(read=False).count()

        unread_messages = unread_recieved_messages + unread_sent_messages

        recieved_message_count = len(inbox)
        reply_num = len(reply_message)
        reply_inbox = len(reply_inbox_message)
        total_reply = reply_num + reply_inbox
        replied_displayed = len(displayed_reply)

        message_count = recieved_message_count + replied_displayed

        print(message_count)
        print(replied_displayed)
        print(recieved_message_count)

        context = {
            'inbox': inbox,
            'message_count': message_count,
            'unread_messages': unread_messages,
            'replied': replied,
            'total_reply': total_reply,
        }
    else:
        inbox = Contacts.objects.all()

        context = {
            'inbox': inbox
        }

    return context
