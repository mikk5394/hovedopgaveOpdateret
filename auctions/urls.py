from django.urls import path
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/auctions')),
    path('auctions/', views.home, name='auctions-home'),
    path('about/', views.about, name='about-us'),
    path('auctionsResult/', views.auctions_result, name='auctions-result')
]
