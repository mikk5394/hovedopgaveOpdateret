from django.shortcuts import render
from .models import Auction


def home(request):
    context = {
        'auctions': Auction.objects.all()
    }
    return render(request, 'auctions/home.html', context)


def about(request):
    return render(request, 'auctions/about.html')
