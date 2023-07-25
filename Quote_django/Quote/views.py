from django.shortcuts import render
import requests

# Create your views here.
def Quote(request):
    category = "inspirational"
    api_url = f"https://api.api-ninjas.com/v1/quotes?category={category}"
    try:
        response = requests.get (api_url, headers={'X-Api-Key': 'c9Ys6JnpsqXdmr7ARqPCFw==YXL1AJg4LStpKrMQ'})
        response.raise_for_status()
        Data = response.json()
        return render(request, 'Quote/Quote.html', {'Quote':Data})    
    except requests.exceptions.RequestException as e:
        print("Error fetching data from api:", e)
        return render(request, "")
