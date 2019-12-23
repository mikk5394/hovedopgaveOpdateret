from django.urls import path
from . import views

urlpatterns = [
    path('auctions/', views.home, name = 'auctions home'),
    path('about/', views.about, name = 'about us'),
]
