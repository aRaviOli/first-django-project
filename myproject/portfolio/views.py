
from django.http import HttpResponse
from django.shortcuts import render
from .models import Portfolio


# Create your views here.
def home(request) -> HttpResponse:
    portfolios = Portfolio.objects.all()
    context = {
        'portfolios': portfolios
    }
    return render(request, 'portfolio/home.html', context)

def about(request) -> HttpResponse:
    return render(request, 'portfolio/about.html')