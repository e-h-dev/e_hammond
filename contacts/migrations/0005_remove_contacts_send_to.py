# Generated by Django 3.2.25 on 2025-01-20 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_contacts_send_to'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacts',
            name='send_to',
        ),
    ]
