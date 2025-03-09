from django.shortcuts import render, redirect, reverse
from django.core.paginator import Paginator
from .models import Reviews
from .forms import ReviewForm


# Create your views here.

def index(request):

    reviews = Reviews.objects.all().order_by('-rating', '-date', '-time')

    paginator = Paginator(reviews, 6)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'reviews': reviews,
        'page_obj': page_obj
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
