from django import forms
from .models import Reviews


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Reviews
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
