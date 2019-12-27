from django.shortcuts import render
from .models import Auction
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    context = {
        'auctions': Auction.objects.all()
    }
    return render(request, 'auctions/home.html', context)


@login_required
def about(request):
    return render(request, 'auctions/about.html')

'''
@login_required
def getAuctions(request):
    

'''