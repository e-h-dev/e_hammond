from .models import Contacts


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





    # read = inbox.read
   
    # for i in inbox:
    #     x = i.read
    #     if x == False:
    #         my_num = x
    #     else:
    #         my_num = 'hello world!'
    #     #print(my_num)
    #     z = []
    #     for my in my_num:
    #         z.append(my)
    #         print(z)
