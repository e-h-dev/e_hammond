from django.contrib import admin
from .models import Contacts, Replied


class ContactAdmin(admin.ModelAdmin):
    readonly_fields = (
        'id',
        # 'name',
        # 'email',
        # 'phone',
        # 'send_to',
        # 'subject',
        # 'message',
        'date',
        'time',
        #'read',
    )

    fields = (
        'id',
        'name',
        'email',
        'phone',
        'send_to',
        'subject',
        'message',
        'date',
        'time',
        'read',
    )

    list_display = (
        'id',
        'name',
        'email',
        'send_to',
        'subject',
        'date',
        'time',
        'date',
        'read',
    )

    ordering = ('-subject',)


admin.site.register(Contacts, ContactAdmin)
admin.site.register(Replied)