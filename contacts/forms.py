from django import forms
from .models import Contacts


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contacts
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
