from django.urls import path
from . import views

app_name = "Quote"

urlpatterns = [
    path('quote', views.Any_Quote, name="Quote"),
    path('<str:category>/quote', views.Quote, name = 'Quote_Category')
]
