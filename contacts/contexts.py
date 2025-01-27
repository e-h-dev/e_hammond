from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Contacts


# @login_required
# def contacts_inbox(request):

#     user = get_object_or_404(User, username=request.user)

#     inbox = Contacts.objects.filter(send_to=user)

#     unread_messages = inbox.filter(read=False).count()

#     print(unread_messages)

    
#     message_count = len(inbox)

#     # print(int(message_count))
    
#     context = {
#         'inbox': inbox,
#         'message_count': message_count,
#         'unread_messages': unread_messages
#     }

#     return context

#@login_required
def contacts_inbox(request):

    inbox = Contacts.objects.all()

    unread_messages = Contacts.objects.filter(read=False).count()

    print(unread_messages)

    
    message_count = len(inbox)

    # print(int(message_count))
    
    context = {
        'inbox': inbox,
        'message_count': message_count,
        'unread_messages': unread_messages
    }

    return context

