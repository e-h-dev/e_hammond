from .models import Contacts


def contacts_inbox(request):

    inbox = Contacts.objects.all()

    #read = inbox.read

    # if Contacts.name:
    #     print(Contacts.objects.name)
    # else:
    #     print('nothing to show')
   
    # for i in inbox:
    #     x = i.read
    #     if x == False:
    #         my_num = x
    #     else:
    #         my_num = 'hello world!'
    #     print(my_num)
        



    message_count = len(inbox)

    # print(int(message_count))
    
    context = {
        'inbox': inbox,
        'message_count': message_count
    }

    return context