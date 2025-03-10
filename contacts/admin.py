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
        'has_reply',
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


class ReplyAdmin(admin.ModelAdmin):
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
        'send_to',
    )

    list_display = (
        'id',
        'name',
        'send_to',
    )


admin.site.register(Contacts, ContactAdmin)
admin.site.register(Replied, ReplyAdmin)
