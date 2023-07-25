from django.urls import path
from . import views

app_name = "Quote"

urlpatterns = [
    path('quote', views.Quote, name="Quote"),
    path('quotes', views.Quote, name = 'Quotes')
]
