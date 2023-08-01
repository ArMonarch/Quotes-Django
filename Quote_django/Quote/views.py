import os
import environ
import requests
from django.shortcuts import render

from .models import Category as CategoryModel

# Initialise environment variables
env = environ.Env()
environ.Env.read_env(os.path.join("../", ".env"))

# Create your views here.
def Quote(request):
    category = request.GET.get("category", "")
    api_key = env('Quote_Api_key')
    api_url = f"https://api.api-ninjas.com/v1/quotes?category={category}"
    try:
        response = requests.get(api_url, headers={'X-Api-Key': api_key})
        response.raise_for_status()
        Data = response.json()
        return render(request, "Quote/Quote.html", {'Quote': Data})
    except requests.exceptions.RequestException as e:
        print("Error fetching data from api:", e)
        return render(request, "")

def Category(request):
    categories = CategoryModel.objects.all()
    return render(request, "Quote/Category.html", {"categories": categories})
