from django.shortcuts import render, get_object_or_404
from .models import Portfolio

# Create your views here.

def all_portfolio(request):
    """
    A view to dispaly all uploaded portfolios, images,
    links and information.
    """
    portfolio = Portfolio.objects.all()

    context = {
        'portfolio': portfolio
    }

    return render(request, "portfolio/portfolio.html", context)


# def full_description(request, id):

#     portfolio = get_object_or_404(Portfolio, id)