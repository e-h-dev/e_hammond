from django.shortcuts import render
from .models import Portfolio

# Create your views here.

def all_portfolio(request):
    portfolio = Portfolio.objects.all()

    context = {
        'portfolio': portfolio
    }

    return render(request, "portfolio/portfolio.html", context)