from django.shortcuts import render
from .models import Reviews

# Create your views here.

def index(request):

    reviews = Reviews.objects.all()

    context = {
        'reviews': reviews,
    }
    
    return render(request, 'home/index.html', context)
