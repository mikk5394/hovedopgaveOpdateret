from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import GetAuctions
from .api_call import get_auctions


@login_required
def about(request):
    return render(request, 'auctions/about.html')


@login_required
def home(request):

    if request.method == 'POST':
        form = GetAuctions(request.POST)
        if form.is_valid():

            region = form.cleaned_data['region']
            server = form.cleaned_data['server']
            amount = form.cleaned_data['amount']

            auctions = get_auctions(region, server, amount)

            context = {
                'form': form,
                'auctions': auctions,
                'total_auctions': get_auctions.number_of_auctions
            }

            return render(request, 'auctions/home.html', context)

    form = GetAuctions()
    return render(request, 'auctions/home.html', {'form': form})
