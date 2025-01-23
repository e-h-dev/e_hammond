from django.contrib import admin
from .models import Contacts


class ContactAdmin(admin.ModelAdmin):
    readonly_fields = (
        'id',
        'name',
        'email',
        'phone',
        'subject',
        'message',
        'date',
        'time',
        'read',
    )

    fields = (
        'id',
        'name',
        'email',
        'phone',
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
        'subject',
        'date',
        'time',
        'date',
        'read',
    )

    ordering = ('-subject',)


admin.site.register(Contacts, ContactAdmin)