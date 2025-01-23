from django.shortcuts import render, redirect, reverse
from .models import Reviews
from .forms import ReviewForm


# Create your views here.

def index(request):

    reviews = Reviews.objects.all().order_by('-rating', '-date', '-time')

    context = {
        'reviews': reviews,
    }
    
    return render(request, 'home/index.html', context)


def create_review(request):
    """
    A view to add reviews and ratings to website
    """
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))

    else:
        form = ReviewForm()

    template = 'home/create_review.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

