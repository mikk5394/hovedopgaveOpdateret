from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import GetAuctions
from .api_call import get_auctions
from .models import Auction
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


@login_required
def about(request):
    return render(request, 'auctions/about.html')


list_of_auctions = []


@login_required
def home(request):
    if request.method == 'POST':
        form = GetAuctions(request.POST)
        if form.is_valid():

            region = form.cleaned_data['region']
            server = form.cleaned_data['server']

            raw_auctions = get_auctions(region, server)

            list_of_auctions.clear()

            for index in range(len(raw_auctions)):
                auc = Auction(raw_auctions[index].get('item'), raw_auctions[index].get('bid'),
                              raw_auctions[index].get('buyout'), raw_auctions[index].get('quantity'),
                              raw_auctions[index].get('timeLeft'))
                # auc.save()
                list_of_auctions.append(auc)

            return redirect('/auctionsResult', list_of_auctions)

    form = GetAuctions()
    return render(request, 'auctions/home.html', {'form': form})


@login_required
def auctions_result(request):
    paginator = Paginator(list_of_auctions, 10)
    page = request.GET.get('page')

    try:
        auc = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        auc = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        auc = paginator.page(paginator.num_pages)

    context = {
        'auctions': auc,
        'total_auctions': get_auctions.number_of_auctions
    }

    return render(request, 'auctions/auctionsresult.html', context)
