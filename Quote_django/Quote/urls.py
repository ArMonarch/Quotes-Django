from django.urls import path
from . import views

app_name = "Quote"

urlpatterns = [
    path('quote', views.Quote, name="Quote"),
    #path('<str:category>/quote', views.Quote, name = 'Quote_Category')
    path("quote?category=value", views.Quote, name = 'Quote_Category'),
    path("category", views.Category, name="Category")
]
