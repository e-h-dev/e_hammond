from django import forms
from .models import Contacts, Replied


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contacts
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        

class ReplyForm(forms.ModelForm):

    class Meta:
        model = Replied
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
