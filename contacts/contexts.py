from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User



from .models import Contacts


def contacts_inbox(request):

    # user = User.objects.all()

    # current_user = user.filter(username='johndoe')

    # print(current_user)

    #user = get_object_or_404(User, username=request.user)

    user = request.user.id
    if user:
        user_inbox = get_object_or_404(User, username=request.user)
        inbox = Contacts.objects.filter(send_to=user_inbox)

        unread_messages = inbox.filter(read=False).count()

        print(unread_messages)

        
        message_count = len(inbox)

        print(int(message_count))
        
        context = {
            'inbox': inbox,
            'message_count': message_count,
            'unread_messages': unread_messages
        }
    else:
        inbox = Contacts.objects.all()

        context = {
            'inbox': inbox
        }

    return context

#@login_required
# def contacts_inbox(request):

#     user = User.objects.all().filter(username='elihammond')

#     print(user)


#     inbox = Contacts.objects.all()

#     unread_messages = Contacts.objects.filter(read=False).count()

#     print(unread_messages)

    
#     message_count = len(inbox)

#     # print(int(message_count))
    
#     context = {
#         'inbox': inbox,
#         'message_count': message_count,
#         'unread_messages': unread_messages,
#     }

#     return context

