# Generated by Django 3.2.25 on 2025-01-16 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ContactUs',
            new_name='Contacts',
        ),
        migrations.AlterModelOptions(
            name='contacts',
            options={'verbose_name_plural': 'Contacts'},
        ),
    ]
