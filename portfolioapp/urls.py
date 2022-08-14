from django.urls import path
from .views import see_portfolio

urlpatterns =[
   path('portfolio/', see_portfolio, name = 'portfolio'),
]